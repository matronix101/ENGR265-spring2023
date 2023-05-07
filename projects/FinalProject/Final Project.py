import json
import os
import numpy as np
import pandas as pd
from IPython.display import display
import plotly.graph_objs as go
from datetime import datetime, timedelta
from IPython.display import display, HTML
from sklearn.datasets import load_iris

# /// Gathering the Data from the JSON files into a Dataframe \\\

# Manually upload the paths of each json file, your file names should be called endsong_0.json~endsong_3.json,
# and endvideo.json, remember to save them as strings or else it won't work
path_0 = 'C:\\Users\\asian\\Downloads\\ENGR265-spring2023\\projects\\FinalProject\\my_spotify_data\\MyData\\endsong_0.json'
path_1 = 'C:\\Users\\asian\\Downloads\\ENGR265-spring2023\\projects\\FinalProject\\my_spotify_data\\MyData\\endsong_1.json'
path_2 = 'C:\\Users\\asian\\Downloads\\ENGR265-spring2023\\projects\\FinalProject\\my_spotify_data\\MyData\\endsong_2.json'
path_3 = 'C:\\Users\\asian\\Downloads\\ENGR265-spring2023\\projects\\FinalProject\\my_spotify_data\\MyData\\endsong_3.json'
path_4 = 'C:\\Users\\asian\\Downloads\\ENGR265-spring2023\\projects\\FinalProject\\my_spotify_data\\MyData\\endvideo.json'
list_of_paths = [path_0, path_1, path_2, path_3, path_4]


# This definition function will be used to just grab and combine all the data from each path
def data_getters(path):
    # Use pandas to convert the JSON into a Dictionary
    with open(path, 'rb') as json_file:
        data = json.load(json_file)

    panda_data = pd.DataFrame.from_dict(data)
    return panda_data


# Getting and combining the JSON data
data_0 = data_getters(path_0)
data_1 = data_getters(path_1)
data_2 = data_getters(path_2)
data_3 = data_getters(path_3)
data_4 = data_getters(path_4)

# Combining all the data into 1 large dataframe
combined_df = pd.concat([data_0, data_1, data_2, data_3, data_4])

# Converting the date time data into a legible format
combined_df['ts'] = combined_df['ts'].str.replace('[TZ]', ' ')

# Getting rid of useless data
list_of_junk = ["username", "platform", "conn_country", "ip_addr_decrypted", "user_agent_decrypted",
                "spotify_track_uri", "episode_name", "episode_show_name", "offline", "offline_timestamp",
                "incognito_mode"]
combined_df = combined_df.drop(list_of_junk, axis=1)


# /// Generating a List of Potential Songs \\\
# Because we are trying to find only one song we only need to find
# the songs that have been played once based on their albums, not their names
# this is because song names are more likely to overlap than the name of the album
def one_time(data):
    one_data = data
    one_data = one_data.drop_duplicates(subset=["master_metadata_album_album_name"])
    return one_data


# /// Generating Filters \\\
# Since there is no perfect filter that can be applied for all, what can be done is having the user choose their filter
# The filters given are, (1) Date Bounds, (2) If the Song was Skipped, (3) If the Song was Not Skipped

# Filter #1: Date Bounds
# From given dates, a bound will be made so that it will only return the data that is within the dates
# Originally, this filter is based on 30 days difference since spotify says it can take up to 1 month to get your data,
# however, if you know the exact dates that you listened to the song, you can implement them

# Unknown Date
end_date = datetime.today()  # Today's Date
start_date = end_date - timedelta(days=30)  # The date 30 days ago


# Known Date
# end_date = datetime(year, month, day) # Input the date in the format of (year, month, day)
# start_date = datetime(year, month, day) # Input the date in the format of (year, month, day)

def date_bounds(data, start_date, end_date):
    data['ts'] = pd.to_datetime(data['ts'])
    date_filter = data[(data['ts'] >= start_date) & (data['ts'] <= end_date)]
    return date_filter


# Filter #2: Skipped
# If the song was skipped, it will return the data that has been skipped
def skipped(data):
    data_filter = data[(data["reason_end"]) == "endplay"]
    return data_filter


# Filter #3: Not Skipped
# If the song was not skipped, it will return the data that was not skipped
def not_skipped(data):
    data_filter = data[(data["reason_end"]) == "trackdone"]
    return data_filter


# /// Combining Filters \\\\
def combined_filters():
    unique_filter = one_time(combined_df)
    date_filter = date_bounds(unique_filter, start_date, end_date)
    unkskiped_filter = not_skipped(date_filter) # The chosen filter was if it was not skipped
    return unkskiped_filter


# /// Reformatting Results \\\
# Once everything is done, we only desire 3 things, the date it played, the song name, and the artist
def reformating():
    final = combined_filters()
    final = final.loc[:, ['ts', "master_metadata_track_name", "master_metadata_album_artist_name"]]
    final = final.rename(columns={'ts': 'Date'})
    final = final.rename(columns={'master_metadata_track_name': 'Song Title'})
    final = final.rename(columns={'master_metadata_album_artist_name': 'Artist'})
    final = final.sort_values('Date', ascending=True)
    return final


# /// Displaying the results \\\

def display_data(df):
    headerColor = 'lightgray'
    rowEvenColor = 'lightblue'
    rowOddColor = 'white'

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=[f'<b>{col_name}</b>' for col_name in df.columns],
            line_color='black',
            fill_color=headerColor,
            align=['left'],
            font=dict(color='black', size=12)
        ),
        cells=dict(
            values=[
                df["Date"],
                df["Song Title"],
                df["Artist"],
            ],
            # line_color='black',
            # 2 dimensional list
            fill_color=[[rowOddColor if i % 2 == 0 else rowEvenColor for i in range(len(df))] * len(df.columns)],
            align=['left'],
            font=dict(color='black', size=11)
        ))
    ])

    fig.update_layout(width=500, height=1000)
    fig.show()


if __name__ == '__main__':
    print(reformating())
    display_data(reformating())
