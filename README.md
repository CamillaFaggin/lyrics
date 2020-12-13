# ASK FOR THE LYRICS OF YOUR FAVORITE ARTIST!

In this repository you can find a file named ```function_main.py```that implements the ```get_lyric( artist, title)``` function. It queries the [lyrics.ovh](https://api.lyrics.ovh/v1/) website to fetch the lyrics of a song```title``` by the specified ```artist``` from the input given by the user.
**Note:** the project requires the following modules to run: *argparse, sqlite3, csv, os, pandas, requests, json, Islice, itemgetter unittest* and *sys*.

# Here's a brief description of each: 
- argparse: By using the argparse module, we implemented -h which provides the User with a "help" message to let him/her better understand the function. Moreover we implemented also --verbosity to give more detailed information.
Subsequently we implemented a required & positional argument that allows the User to run the function n* times:  if I insert 2, the User will be able to perform only 2 queries, thus obtaining the lyrics of 2 songs.
- get_lyrics: It queries the link https://api.lyrics.ovh/v1/ with the inputs given by the User. 
With the module csv we created a csv file ("lyrics.csv") in which we can find the authors, artist's name and lyrics that the user chose as an input.We state to print out just the first 5 lines of the given song's lyrics. If an error message is returned, the User must redo the query.
- fun_sqlite: By using the sqlite3 module, the function creates a database ("lyrics.db") comprising the research made by the User. The print function shall return the database containing the artist's name, the song's title and its lyrics, researched n* times.

The project uses the ```json```, ```requests```, ```argparse```, ```sqlite3```, ```csv```, ```Islice```, ```itemgetter``` modules.

# Documentation
Documentation can be found in: https://api.lyrics.ovh/v1/ website where it is possible to find information about artists, their songs' titles and the related lyrics. All of this data is going to be used throughout the project. 

# Data Files
Songs' lyrics data is stored in a .csv file called "lyrics.csv".

```
If you run the program, executing the main file with: ```function_main.py``` it will give you results similar to the following:
...
``` 
$ function_main.py
Yellow by Coldplay:
"Look at the stars
nlook how they shine for you
and everything you do
yeah they were all yellow
I came along
I wrote a song for you
and all the things you do
and it was called yellow


# Testing 
Tests on parts of the code are provided here: 
\\\\\\\\\\\\\\\\\\\\\

You can find the following modules:\\\\\\\\\\\\\\\

To run it from the main folder use:\\\\\\\\\\\\\\\\



# Authors and acknowledgment
Thank you all for the collaboration! 
- [**Giulia Angelini**]
- [**Camilla Faggin**]
- [**Dayana Manfredi**]
- [**Francesca Zecchinato**]