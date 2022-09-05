import glob
import csv
import json
import time
import sys
import os
import zipfile
import shutil

zf = None

def explore():
    # Variables
    total_messages = 0
    total_channels = 0
    friend_list = []
    server_list = []
    group_list = []

    # Create server list
    server_index_file = open(f'{extracted_path}/package/servers/index.json')
    server_data = json.load(server_index_file)
    server_index_file.close()

    # Populate server list
    for row in server_data:
        if len(server_data[row]) > 27: 
            server_list.append((row, server_data[row][:27] + "...", 0))
        else:
            server_list.append((row, server_data[row], 0))

    # Get user data
    user_file = open(f'{extracted_path}/package/account/user.json')
    user_data = json.load(user_file)
    user_file.close()
    user_id = user_data['id']

    for file in glob.glob(f'{extracted_path}/package/messages/**/*.csv', recursive=True):
        message_file = open(file, errors="ignore")
        reader = csv.DictReader(message_file)

        file_total_messages = 0
        total_channels += 1

        for row in reader:
            file_total_messages += 1


        total_messages += file_total_messages
        message_file.close()

        # Check what the channel is
        channel_file_location = file.replace('messages.csv', 'channel.json')
        channel_file = open(channel_file_location)
        channel_data = json.load(channel_file)
        channel_file.close()

        # Get all server messages
        if channel_data['type'] == 0:
            try:
                server_id = channel_data['guild']['id']
                for i in range(len(server_list)):
                    if server_list[i][0] == server_id:
                        temp_list = list(server_list[i])
                        temp_list[2] += file_total_messages
                        server_list[i] = tuple(temp_list)
            except:
                pass

        # Get friend
        if channel_data['type'] == 1:
            try:
                recipients = channel_data['recipients']
                for recipient in recipients:
                    if recipient != user_id:
                        friend_id = recipient

                for relationship in user_data['relationships']:
                    if relationship['id'] == friend_id:                        
                        friend_username = relationship['user']['username']
                        if len(friend_username) > 30:
                            friend_username = friend_username[:24] + "..."
                        friend = [friend_id, friend_username, file_total_messages]
                        friend_list.append(friend)
            except:
                pass

        # Get best groupchat
        if channel_data['type'] == 3:
            try:
                if len(channel_data['name']) > 30:
                    channel_data['name'] = channel_data['name'][:27] + "..."
                group = [channel_data['id'], channel_data['name'], file_total_messages] # [:30]Trunacates itr
                group_list.append(group)
            except:
                pass

    # Outputs
    friend_list = quick_sort(friend_list)
    server_list = quick_sort(server_list)
    group_list = quick_sort(group_list)

    for i in range(len(group_list)):
        if group_list[i][1] is None:
            group_list[i][1] = "Default Groupname"

    return total_messages, friend_list, server_list, group_list, total_channels

# Quick Sort Algorithm
def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        left = []
        right = []
        for i in range(1, len(list)):
            if list[i][2] < list[0][2]:
                right.append(list[i])
            else:
                left.append(list[i])
    return(quick_sort(left) + list[:1] + quick_sort(right))

def main(filename):

    # Allows unicode on Windows console
    sys.stdout.reconfigure(encoding='utf-8')

    global extracted_path, package_path
    extracted_path = os.getcwd() + f'/temp/{filename.split(".", 1)[0]}'
    package_path = os.getcwd() + f'/temp/{filename}'
    
    start_time = time.time()

    zf = zipfile.ZipFile(package_path, 'r')
    zf.extractall(extracted_path)
    zf.close()

    print("Extracted! Time taken: ", time.time() - start_time)

    start_time = time.time()
    result = explore()
    print("Explored! Time taken: ", time.time() - start_time)

    # Remove extracted files & zip files
    shutil.rmtree(extracted_path)
    os.remove(package_path)
    
    return result
