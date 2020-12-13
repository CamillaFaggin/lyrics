# ASK FOR THE LYRICS OF YOUR FAVORITE ARTIST! :musical_note:

In this repository you can find a file named ```main.py```that implements the ```get_lyric( artist, title)``` function. It queries the [lyrics.ovh](https://api.lyrics.ovh/v1/) website to fetch the lyrics of a song```title``` by the specified ```artist``` from the input given by the user.
**Note:** the project requires the following modules to run: *argparse, sqlite3, csv, os, pandas, requests, json, Islice, itemgetter unittest* and *sys*.

# Here's a brief description of each: :book:
- argparse: By using the argparse module, we implemented -h which provides the User with a "help" message to let him/her better understand the function. Moreover we implemented also --verbosity to give more detailed information.
Subsequently we implemented a required & positional argument that allows the User to run the function n* times:  if I insert 2, the User will be able to perform only 2 queries, thus obtaining the lyrics of 2 songs.
- get_lyrics: It queries the link https://api.lyrics.ovh/v1/ with the inputs given by the User. 
With the module csv we created a csv file ("lyrics.csv") in which we can find the authors, artist's name and lyrics that the user chose as an input.We state to print out just the first 5 lines of the given song's lyrics. If an error message is returned, the User must redo the query.
- fun_sqlite: By using the sqlite3 module, the function creates a database ("lyrics.db") comprising the research made by the User. The print function shall return the database containing the artist's name, the song's title and its lyrics, researched n* times.

The project uses the ```json```, ```requests```, ```argparse```, ```sqlite3```, ```csv```, ```Islice```, ```itemgetter```, ```unittest```, ```sys```, ```os``` modules.


# Documentation :book:
Documentation can be found in: https://api.lyrics.ovh/v1/ website where it is possible to find information about artists, their songs' titles and the related lyrics. All of this data is going to be used throughout the project. 

# Data Files :file_folder:
Songs' lyrics data is stored in a .csv file called "lyrics.csv".

```
If you run the program, executing the main file with: ```main.py``` it will give you results similar to the following:
...
``` 
$ main.py
Heroes by David Bowie:
I, I, will, be, king
And, you, you, will, be, queen
Though, nothing, will, drive, them, away
We, can, beat, them,, just, for, one, day


# Testing :cop:

You can find the following modules:
```json```, ```requests```, ```argparse```, ```sqlite3```, ```csv```, ```Islice```, ```itemgetter```, 
```unittest```, ```sys```, ```os```.

To run it, use: 
python -m unittest -v -b test.py

In order to make the command work, 
you must be in the folder test_lyrics.



# Authors and acknowledgment :computer:
Thank you all for the collaboration! 
- *Giulia Angelini*
- *Camilla Faggin*
- *Dayana Manfredi*
- *Francesca Zecchinato*