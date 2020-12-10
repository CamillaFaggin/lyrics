import unittest
from Function_main import get_lyrics
import os
#python -m unittest /test_lyrics/test_main.py

class TestMain(unittest.TestCase):

    # setUp function prepare some data for tests
    def setUp(self):
        # create an empty file
        # note: this would be better done with tempfile
        self.temporary_file = "/tmp/emptyfile.csv"
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
        d = get_lyrics() 
        self.assertFalse(d)


    def test_empty_datafie(self):
        d = Function_main.get_lyrics(self.temporary_file) 
        self.assertFalse(d)


    # tearDown function cleans the temporary data
    def tearDown(self):
        os.remove(self.temporary_file)


if __name__ == "__main__":
    unittest.main(verbosity=2)