import unittest

def digits(x):
    """COnvert an integer into a list of digits.

    Args:
        x : The number whose digits we want.abs
    >>>digits(4586378)
        [4, 5, 8, 6, 3, 7, 8]
    """
    # import pdb; pdb.set_trace()
    digs = []
    while x!= 0:
        div, mod = divmod(x, 10)
        digs.append(mod)
        x=div
    return digs

def is_palindrome(x):
    """Determine if an integer is a palindrome.abs

    Args:
        x : The number to check for palindromicity.abs

    Returns: True if the digits of ''x '' are a palindrome otherwise False
    """

    digs = digits(x)
    for f, r in zip(digs, reversed(digs)):
        if f != r:
            return False
    return True

class Tests(unittest.TestCase):
    """Tests for the is_plaindrome function. """

    def test_negative(self):
        """Check that it returns False correctly"""
        self.assertFalse(is_palindrome(1234))

    def test_positive(self):
        """Check that it returns True correctly"""
        self.assertTrue(is_palindrome(1221))

    def test_single_digit(self):
        """Check that it works for a single digit number"""
        for i in range(10):
            self.assertTrue(is_palindrome(1))

if __name__ == '__main__':
    unittest.main()
