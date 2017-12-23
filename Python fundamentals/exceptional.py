"""A module for demonstarting exceptions"""

import sys

def convert(s):
    """Convert to an integer"""
    try:
        return int(s)
    # except ValueError:
    #     print("Conversion failed")
    #     x=-1
    # except TypeError:
    #     print("Conversion Failed")
    #     x=-1
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)),
            file=sys.stderr)
        return -1