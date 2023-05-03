import json
import os
import numpy as np
import pandas as pd

# /// Combining all the JSON files into one MEGA dictionary \\\

# Creating an empty "dictionary" that we will add all the JSON files to
spotify_data_dict = {}

# Upload the path to the folder of JSON files
# Remember to save them as strings or else it won't work
folder_of_json_paths = 'C:\\Users\\asian\\Downloads\\ENGR265-spring2023\\projects\\FinalProject\\my_spotify_data\\MyData'

# Checking to see if the folder is accessible and data can be grabbed

path = 'C:\\Users\\asian\\Downloads\\ENGR265-spring2023\\projects\\FinalProject\\my_spotify_data\\MyData\\endsong_1.json'

#print(type(path)) // Checks path
#This opens the path to the file
with open(path,'rb') as json_file:
    data = json.load(json_file)


panda_data = pd.DataFrame.from_dict(data)
print(panda_data)

    #,"ms_played","master_metadata_track_name","master_metadata_album_artist_name","master_metadata_album_album_name","episode_name","reason_start","reason_end", "shuffle","skipped"
    #print(type(data[0]))
    #print(data[0])
    #print(data[1])
    #print(data[2])
    #print(data[10])
    #print(data[-1])
    #print(data)

# Create a for loop that will go through the folder add them to the dictionary
#for json_file in os.listdir(folder_of_json_paths):
#    if json_file.endswith('.json'):  # Check the contents
#        print(f'Wow it opened this path \n{folder_of_json_paths}')  # Sees if there are files
#        with open(os.path.join(folder_of_json_paths, json_file), 'r') as json_file_data:
#            extracted_data = json.loads(json_file_data)
#        # Pull only the useful data that we want
#        spotify_data_dict[json_file] = extracted_data

# {
#                "ts": extracted_data['ts'],
#                "ms_played": extracted_data["ms_played"],
#                "master_metadata_track_name": extracted_data["master_metadata_track_name"],
#                "master_metadata_album_artist_name": extracted_data["master_metadata_album_artist_name"],
#                "master_metadata_album_album_name": extracted_data["master_metadata_album_album_name"],
#                "episode_name": extracted_data["episode_name"],
#                "reason_start": extracted_data["reason_start"],
#                "reason_end": extracted_data["reason_end"],
#                "shuffle": extracted_data["shuffle"],
#                "skipped": extracted_data["skipped"],
#            }
# /// Extracting only useful data in the dictionary \\\
# Go through the dictionary and only grab the useful information
# The useful information that we only need are as follows (and in order)
# The date that it was accessed, how long it was playing, the name of the song, the artist name, the album name,
# reason why it was started, why did it end, if it was shuffled, and if it was skipped

# Here is an example of what each element in the dictionary looks like, also a '*' will signify if used
# "ts":"2022-12-03T17:00:38Z" !T (numbers) Z! represents the time start *
# "username":"22ziyllkwb2ilbeedq5vzidcy"
# "platform":"ios"
# "ms_played":0
# "conn_country":"US"
# "ip_addr_decrypted":"(two numbers).(three numbers).(two numbers).(two numbers)" !We do not look at the IP Address!
# "user_agent_decrypted":"unknown"
# "master_metadata_track_name":"声?" *
# "master_metadata_album_artist_name":"はてな" *
# "master_metadata_album_album_name":"声?" *
# "spotify_track_uri":"spotify:track:00EAiVX99rZ4rlYFLItPcC"
# "episode_name":null *
# "episode_show_name":null
# "spotify_episode_uri":null
# "reason_start":"unknown" *
# "reason_end":"endplay" *
# "shuffle":false *
# "skipped":true *
# "offline":null
# "offline_timestamp":0
# "incognito_mode":false
