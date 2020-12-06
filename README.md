In this repository you can find a file named ```function_main.py```that implements the ```get_lyric( artist, title)``` function. It queries the [lyrics.ovh](https://api.lyrics.ovh/v1/) website to fetch the lyrics of a song```title``` by the specified ```artist``` from the input given by the user.
In the program it is possibile to find the following functions: argparse, get_lyrics, fun_sqlite.

Here's a brief description of each: 
- argparse: By using the argparse module, we implemented -h which provides the User with a "help" message to let him/her better understand the function. 
Subsequently we implemented a required & positional argument that allows the User to run the function n* times:  if I insert 2, the User will be able to perform only 2 queries, thus obtaining the lyrics of 2 songs.
- get_lyrics: It queries the link https://api.lyrics.ovh/v1/ with the inputs given by the User. 
Being inserted in the csv file ("lyrics.csv"), we state to print out just the first 5 lines of the given song's lyrics. If an error message is returned, the User must redo the query.
- fun_sqlite: By using the sqlite3 module, the function creates a database ("lyrics.db") comprising the research made by the User. The print function shall return the database containing the artist's name, the song's title and its lyrics, researched n* times.

The project uses the ```json```, ```requests```, ```argparse```, ```sqlite3```, ```csv```, ```Islice```, ```itemgetter``` modules.

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


