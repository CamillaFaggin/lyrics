import json
import requests
import csv
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("get info", help="The function gives the lyrics of a song n times")
    args = parser.parse_args()


    parser = argparse.ArgumentParser()
    parser.add_argument("x")
    args = parser.parse_args()
    print(args.x) 

    for i in range (int(args.x)):
        print(i+1,'song')
        get_lyrics()

def get_lyrics():
    base_url = "https://api.lyrics.ovh/v1/"
    
    print()
    
    artist_name=input('Write the artist name here: ')
    song_title=input('Write the song name here: ')
    
    search_url = base_url + artist_name + '/' + song_title
    
    print()
    print()
    
    req = requests.get(search_url)
    dict_lyrics=req.json()
    list_lyr=dict_lyrics['lyrics']
    
    with open('lyrics.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["artist", "song", "lyrics"])
        writer.writerow([artist_name, song_title, list_lyr])

    
    csv.register_dialect('csv_dialect',
                    delimiter='|',
                    skipinitialspace=False,
                    quoting=csv.QUOTE_ALL)
    
    with open('lyrics.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=" ", quotechar='|')
        for row in reader:
            print(', '.join(row))
            
    
    if len(list_lyr) == 0 :
        print("We haven't found a lyrics for your research.")
        print("Please verify that you haven't mispelled, or try changing your song.")    
           
        
    else:
        print('The lyrics is: ')
        
    
    print( list_lyr )
    

main()
