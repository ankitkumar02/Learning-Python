import os
import unittest

def analyze_text(filename):
    """CAlculate the number of lines and characters in a  file
    
    Args:
        filename : The name of the file to analyze

    Raises:
        IOError : If filename does not exist or cant be read.

    Returns: A tuple where the first argument is the number of lines in the file and the second element
        is the number of characters.
    """
    lines = 0
    chars = 0

    with open(filename, 'r') as f:
        for line in f:
            lines +=1
            chars += len(line)
        return lines, chars

class TextAnalysisTests(unittest.TestCase):
    """Tests for the ''analyze_text()'' function."""

    def setUp(self):
        """Fixture that creates a file for the test methods to use"""

        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war. \n'
                    'testing whether that nation , \n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure.')
    
    def tearDown(self):
        """Fixture thet deletes the file created for the test methods"""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """BAsic smoke test : does the function run.."""
        analyze_text(self.filename)
    
    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_character_count(self):
        """Check the character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1], 134)
    
    def test_no_such_file(self):
        """Check the proper exception is thrown for the missing file."""
        with self.assertRaises(IOError):
            analyze_text('foobar')
    
    def test_no_deletion(self):
        """Check whether the function doesn't delete the file."""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    unittest.main()

