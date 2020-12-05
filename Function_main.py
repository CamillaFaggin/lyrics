import json
import requests
import csv
import argparse
import sqlite3

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

    def fun_sqlite():
        list_lyr2=list_lyr.replace('\r\n',' ')
        list_lyr2=list_lyr2.replace('\n',' ')
        list_lyr2=list_lyr2.replace('\r',' ')
        list_lyr3=list_lyr2                      
        
        conn1 = sqlite3.connect('lyrics.db')
        curs1 = conn1. cursor ()
        curs1.execute('''CREATE TABLE ly5 (artist_name, song_title, lyrics)''')
        curs1.execute("INSERT INTO ly5 VALUES (?,?,?)",  (artist_name, song_title, list_lyr3))

        r=curs1.execute('SELECT * FROM ly5 ').fetchall()
        for row2 in r:
            print(row2)

        conn1.commit()
        conn1.close()
    print()    
    print('Database from sqlite')
    print(fun_sqlite())       

fun_sqlite = get_lyrics

get_lyrics()
main()
