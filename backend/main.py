from zipfile import ZipFile
from shutil import rmtree
from random import randint
from glob import glob
import time
import os
import json
import datetime
import ujson


class Discord:
    # Set default values for the data.
    def __init__(self):
        self.user_id = ""
        self.browsers = {}
        self.events = {}
        self.payment_total = 0
        self.predicted_age = "Unknown"
        self.message_analytics = {
            "friends": {},
            "servers": {},
            "groups": {},
            "messages_to_friends": 0,
            "messages_to_nonfriends": 0,
            "everyone_mentions": 0,
            "total_words": 0,
            "total_length": 0,
            "total_messages": 0
        }
        self.activity_analytics = {
            "hourly": {},
            "weekly": {}
        }

    # Extract the Zip file

    def extract_data(self, filename):
        start_time = time.time()
        self.filepath = f'{os.getcwd()}/temp/{filename}'
        self.folder = f'{randint(0, 1000)}'

        with ZipFile(self.filepath, 'r') as zf:
            for file in zf.namelist():
                if file.startswith('package/account/user.json') or file.startswith('package/activity/analytics/') or file.startswith('package/servers/index.json') or file.startswith('package/messages/'):
                    zf.extract(file, f'temp/{self.folder}')

        # Delete the Zip file
        os.remove(f'{os.getcwd()}/temp/{filename}')
        print(f"Time to extract data: {time.time() - start_time} seconds")

    # Get User ID

    def get_user(self):
        with open(f'temp/{self.folder}/package/account/user.json') as user:
            data = json.load(user)
            self.user_id = data['id']
            self.relationships = data['relationships']

            # Get friends
            for friend in data['relationships']:
                self.message_analytics['friends'][friend['id']] = {
                    'name': friend['user']['username'], 'messages': 0, 'avatar': friend['user']['avatar']}

            # Get payment total
            for payment in data['payments']:
                self.payment_total += payment['amount']

    # Get all the servers

    def get_servers(self):
        with open(f'temp/{self.folder}/package/servers/index.json') as index:
            servers = json.load(index)
            for row in servers:
                self.message_analytics['servers'][row] = {
                    'name': servers[row], 'messages': 0}

    def get_analytics(self):
        # Open all the files
        for file in glob(f'temp/{self.folder}/package/activity/analytics/*.json', recursive=True):
            with open(file) as f:
                for line in f:
                    data = ujson.loads(line)

                    # Get message analytics
                    self.get_message_analytics(data)

                    # Get activity data
                    if "_hour_utc" in data.keys():
                        # Hourly  activity
                        hour = data['_hour_utc'].split('T')[1][:2]
                        if hour in self.activity_analytics['hourly']:
                            self.activity_analytics['hourly'][hour] += 1
                        else:
                            self.activity_analytics['hourly'][hour] = 1

                        # Daily activity
                        date = datetime.datetime.strptime(
                            data['_hour_utc'], "%Y-%m-%dT%H:%M:%S")
                        weekday = date.strftime("%A")

                        if weekday in self.activity_analytics['weekly']:
                            self.activity_analytics['weekly'][weekday] += 1
                        else:
                            self.activity_analytics['weekly'][weekday] = 1

                    # Get the predicted age
                    if "predicted_age" in data.keys():
                        self.predicted_age = data['predicted_age']

                    # Get the events
                    if "event_type" in data.keys():
                        if data['event_type'] in self.events:
                            self.events[data['event_type']] += 1
                        else:
                            self.events[data['event_type']] = 1

                    # Get the browsers the user uses
                    if "browser" in data.keys():
                        if data['browser'] in self.browsers:
                            self.browsers[data['browser']] += 1
                        else:
                            self.browsers[data['browser']] = 1

    def get_message_analytics(self, data):
        if "event_type" in data.keys():
            if data['event_type'] == "send_message" and "channel_type" in data.keys():
                self.message_analytics['total_messages'] += 1

                # Get additonal message analytics
                # Get @everyones
                if "mention_everyone" in data.keys():
                    if data['mention_everyone'] in self.message_analytics:
                        if data['mention_everyone']:
                            self.message_analytics["everyone_mentions"] += 1

                # Get total length of messages, and total words sent
                if "length" in data.keys():
                    self.message_analytics["total_length"] += int(
                        data['length'])

                if "word_count" in data.keys():
                    self.message_analytics["total_words"] += int(
                        data['word_count'])

                # Get the total messages friends, servers & groups sent
                try:
                    with open(f'temp/{self.folder}/package/messages/c{data["channel"]}/channel.json') as f:
                        channel_data = json.load(f)

                        # If friend DM
                        if data['channel_type'] == "1":
                            # Get messages sent to friends & non friends
                            if data['is_friend']:
                                self.message_analytics["messages_to_friends"] += 1
                            else:
                                self.message_analytics["messages_to_nonfriends"] += 1

                            # Get the total messages sent to each friend
                            for recipiant in channel_data['recipients']:
                                if recipiant != self.user_id:
                                    for relation in self.relationships:
                                        if recipiant == relation['id']:
                                            if recipiant in self.message_analytics['friends'].keys():
                                                self.message_analytics['friends'][recipiant]['messages'] += 1
                            return

                        # If server
                        elif data['channel_type'] == "0":
                            if channel_data['guild']['id'] in self.message_analytics['servers'].keys():
                                self.message_analytics['servers'][channel_data['guild']
                                                                  ['id']]['messages'] += 1
                            return

                        # If group
                        elif data['channel_type'] == "3":
                            if channel_data['id'] in self.message_analytics['groups'].keys():
                                self.message_analytics['groups'][channel_data['id']
                                                                 ]['messages'] += 1
                            else:
                                if channel_data['name'] == None:
                                    channel_data['name'] = "Unnamed Group"

                                self.message_analytics['groups'][channel_data['id']] = {
                                    'name': channel_data['name'], 'messages': 1}

                            return

                except:
                    return

    def sort_data(self):
        # Each dict has a key which is id then a sub dict with messages inside, sort the dict by the messages key so most messages is 0, return as a list/array
        self.message_analytics['friends'] = sorted(
            self.message_analytics['friends'].items(), key=lambda d: d[1]['messages'], reverse=True)
        self.message_analytics['servers'] = sorted(
            self.message_analytics['servers'].items(), key=lambda d: d[1]['messages'], reverse=True)
        self.message_analytics['groups'] = sorted(
            self.message_analytics['groups'].items(), key=lambda d: d[1]['messages'], reverse=True)

        # Sort the activity analytics
        sorted_weekdays = []
        weekdays_order = ["Monday", "Tuesday", "Wednesday",
                          "Thursday", "Friday", "Saturday", "Sunday"]
        for day in weekdays_order:
            if day in self.activity_analytics['weekly']:
                sorted_weekdays.append(
                    (day, self.activity_analytics['weekly'][day]))
            else:
                sorted_weekdays.append((day, 0))
        self.activity_analytics['weekly'] = sorted_weekdays

        # Sort the hours
        sorted_hours = []
        hours_order = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                       '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
        for hour in hours_order:
            if int(hour) > 12:
                display_hour = f"{int(hour) - 12}pm"
            elif hour == 12:
                display_hour = f"{int(hour)}pm"
            else:
                display_hour = f"{int(hour)}am"

            if hour in self.activity_analytics['hourly']:
                sorted_hours.append(
                    (display_hour, int(self.activity_analytics['hourly'][hour])))
            else:
                sorted_hours.append((hour, 0))

        self.activity_analytics['hourly'] = sorted_hours

    def get_data(self):
        start_time = time.time()
        self.get_user()
        print(f"Time to get user: {time.time() - start_time} seconds")

        func_time = time.time()
        self.get_servers()
        print(f"Time to get servers: {time.time() - func_time} seconds")

        func_time = time.time()
        self.get_analytics()
        print(f"Time to get analytics: {time.time() - func_time} seconds")

        func_time = time.time()
        self.sort_data()
        print(f"Time to sort users: {time.time() - func_time} seconds")

        # Delete folder
        rmtree(f'{os.getcwd()}/temp/{self.folder}')

        # Time taken
        print(f"--- {time.time() - start_time} seconds ---")

        return {
            'message_analytics': self.message_analytics,
            'activity_analytics': self.activity_analytics,
            'events': self.events,
            'browsers': self.browsers,
            'payment_total': self.payment_total,
            'predicted_age': self.predicted_age,
        }


def main(filename):
    data = Discord()
    data.extract_data(filename)
    return data.get_data()


if __name__ == '__main__':
    main()
