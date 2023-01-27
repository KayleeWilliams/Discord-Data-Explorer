import os
from zipfile import ZipFile
from glob import glob
import json
import csv
from shutil import rmtree
from random import randint


class Discord:
  # Set default values for the data.
  def __init__(self):
    self.total_messages = 0
    self.total_channels = 0
    self.friends = []
    self.servers = []
    self.groups = []
    self.browsers = {}
    self.events = {}


  # Extract the Zip file
  def extract_data(self, filename):
    self.filepath = f'{os.getcwd()}/temp/{filename}'
    self.folder = f'{randint(0, 1000)}'

    with ZipFile(self.filepath, 'r') as zf:
      zf.extractall(f'temp/{self.folder}')
    
    # Delete the Zip file 
    os.remove(f'{os.getcwd()}/temp/{filename}')

  # Get User ID
  def get_user(self):
    with open(f'temp/{self.folder}/package/account/user.json') as user:
      data = json.load(user)
      self.user_id = data['id']
      self.relationships = data['relationships']

  # Get all the servers
  def get_servers(self):
    with open(f'temp/{self.folder}/package/servers/index.json') as index:
      servers = json.load(index)
      for row in servers:
        self.servers.append({'id': row, 'name': servers[row], 'messages': 0})

  def file_data(self, file):
    file_messages = 0
    self.total_channels += 1

    # Get messages
    with open(file, errors='ignore') as mf:
      messages = csv.DictReader(mf)
      for row in messages:
        file_messages += 1

    self.total_messages += file_messages 

    # Get channel
    with open(file.replace('messages.csv', 'channel.json')) as cf:
      channel = json.load(cf)
    
    # If server
    if channel['type'] == 0 and 'guild' in channel:
      server_id = channel['guild']['id']
      for i, server in enumerate(self.servers):
        if server['id'] == server_id:
          server['messages'] += file_messages

    # If friend
    if channel['type'] == 1 and 'recipients' in channel:
      for recipient in channel['recipients']:
        if recipient != self.user_id:
          for relationship in self.relationships:
            if relationship['id'] == recipient:
              self.friends.append({'id': recipient, 'name': relationship['user']['username'], 'messages': file_messages, 'avatar': relationship['user']['avatar']})

    # If groupchat
    if channel['type'] == 3 and 'name' in channel:
      if channel['name'] != None: 
        self.groups.append({'id': channel['id'], 'name': channel['name'], 'messages': file_messages})
      else: 
        self.groups.append({'id': channel['id'], 'name': 'Unnamed Group', 'messages': file_messages})

  def get_analytics(self):
    for file in glob(f'temp/{self.folder}/package/activity/analytics/*.json', recursive=True):
      with open(file) as f:
        for line in f:
          data = json.loads(line)
          if data['event_type'] in self.events:
            self.events[data['event_type']] += 1
          else:
            self.events[data['event_type']] = 1

          # Get the browsers the user uses
          if "browser" in data: 
            if data['browser'] in self.browsers:
              self.browsers[data['browser']] += 1
            else:
              self.browsers[data['browser']] = 1
    
  def sort_data(self):
    self.friends = sorted(self.friends, key=lambda d: d['messages'],  reverse=True)
    self.servers = sorted(self.servers, key=lambda d: d['messages'],  reverse=True)
    self.groups = sorted(self.groups, key=lambda d: d['messages'],  reverse=True)

  def get_data(self):
    self.get_user()
    self.get_servers()
    self.get_analytics()

    for file in glob(f'temp/{self.folder}/package/messages/**/*.csv', recursive=True):
      self.file_data(file)

    self.sort_data()

    # Delete folder
    rmtree(f'{os.getcwd()}/temp/{self.folder}')

    return {
      'total_messages': self.total_messages, 
      'total_channels': self.total_channels, 
      'friends': self.friends,
      'servers': self.servers,
      'groups': self.groups,
      'browsers': self.browsers,
      'events': self.events
    }

def main(filename):
  data = Discord()
  data.extract_data(filename)
  return data.get_data()

if __name__ == '__main__':
  main()