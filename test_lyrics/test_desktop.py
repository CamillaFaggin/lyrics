import unittest
import sys
import os

# add parent folder to path
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__name__))))
#sys.path.append("/test_lyrics/test_main.py/")
from test_main import get_lyrics


class TestInput(unittest.TestCase):

    # smoke test: valid inputs
    #def test_correct_values(self):
        # you should select some valid inputs, for which the output is known
        #self.assertEqual(main(), int(args.x) )
        
           

    # invalid inputs
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(get_lyrics("artist", "song"), None )
            
        

        

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(get_lyrics(" ", " "), None)
        self.assertEqual(get_lyrics("Coldplay", " "), None)
        self.assertEqual(get_lyrics(" ", "Yellow"), None)
            


if __name__ == '__test_main.py__' :
    
    # basic test
    #unittest.main()
    unittest.get_lyrics()

    # with more details
    #unittest.get_lyrics(verbosity=2)