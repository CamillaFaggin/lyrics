import json
import requests
import csv
import argparse
import sqlite3
import sys
import os

sys.path.append("/KEEPtest_main.py/")
from KEEPtest_main import get_lyrics

def fun_sqlite():
    
    list_lyr2=get_lyrics(list_lyr.replace('\r\n',' '))
    list_lyr2=list_lyr2.replace('\n',' ')
    list_lyr2=list_lyr2.replace('\r',' ')
    list_lyr3=list_lyr2                      
        
    conn1 = sqlite3.connect('lyrics.db')
    curs1 = conn1. cursor ()
    #curs1.execute('''CREATE TABLE ly5 (artist_name, song_title, lyrics)''')
    curs1.execute("INSERT INTO ly5 VALUES (?,?,?)",  (artist_name, song_title, list_lyr3))

    r=curs1.execute('SELECT * FROM ly5 ').fetchall()
    for row2 in r:
        print(row2)

    conn1.commit()
    conn1.close()
    print()    
    print('Database from sqlite')
    print(fun_sqlite())    
fun_sqlite()
