import json
import requests
import csv
import argparse
import sqlite3
from itertools import islice
from operator import itemgetter


def get_lyrics(artist, song):
    base_url = "https://api.lyrics.ovh/v1/"
    artist_name=artist
    song_title=song

    search_url = base_url + artist_name + '/' + song_title
    req = requests.get(search_url)
    status = req.status_code
    if status==404:
        print("Invalid research. Retry")
    
    else: 
        dict_lyrics = req.json()
        list_lyr = dict_lyrics['lyrics']
        
        if len(list_lyr) == 0:
            print("We haven't found a lyrics for your research.")
            print("Please verify that you haven't mispelled, or try changing your song.")

        else:
            with open('lyrics.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["artist", "song", "lyrics"])
                writer.writerow([artist_name, song_title, list_lyr])

            csv.register_dialect('csv_dialect', delimiter='|', skipinitialspace=False,
                                     quoting=csv.QUOTE_ALL)
#  first 5 only
            with open('lyrics.csv', 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=" ", quotechar='|')
                for row in islice(reader, 5):
                    print(', '.join(row))
        
artist=input('Write the artist name here: ')
song=input('Write the song name here: ')    
get_lyrics(artist, song)

    

