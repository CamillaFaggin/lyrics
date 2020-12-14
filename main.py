'''import libraries and modules''' 
import json
import requests
import csv
import argparse
import sqlite3
from itertools import islice
from operator import itemgetter

'''implementing argparse'''
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("get info", help="Firstly, Insert a n. of songs you want")
    parser.add_argument("-- verbosity", help="Consequently, n. lyrics are displayed.",
                        action="store_true")
    args = parser.parse_args()

    parser = argparse.ArgumentParser()
    parser.add_argument("x")
    args = parser.parse_args() 
    print(args.x) 

    for i in range(int(args.x)):
        print(i+1, 'song')
        get_lyrics()


def get_lyrics():
    base_url = "https://api.lyrics.ovh/v1/"
#define the input values
    artist_name = input('Write the artist name here: ')
    song_title = input('Write the song name here: ')

    search_url = base_url + artist_name + '/' + song_title
    req = requests.get(search_url)
    status = req.status_code
    if status == 404:
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

        def fun_sqlite():
            list_lyr2 =list_lyr.replace('\r\n ', ' ')
            list_lyr2 =list_lyr2.replace('\n ', ' ')
            list_lyr2 =list_lyr2.replace('\r', ' ')
            list_lyr3 =list_lyr2                     
        
            conn1 = sqlite3.connect('lyrics.db')
            curs1 = conn1. cursor()
            #curs1.execute('''CREATE TABLE tablelyr1 (artist_name, song_title, lyrics)''')
            curs1.execute("INSERT INTO tablelyr1 VALUES (?,?,?)",  (artist_name, song_title, list_lyr3))
            r = curs1.execute('SELECT * FROM tablelyr1').fetchall() 
            print()
            for row2 in r:
                print (row2)

            conn1.commit()
            conn1.close()
            print('Database from sqlite')
        fun_sqlite()

fun_sqlite=get_lyrics



main()





