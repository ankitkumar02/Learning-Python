"""Retrieve and prints words from a URL.

Usage :

    python3 words.py <URL>
"""
import sys
from urllib.request import urlopen


#  url == http://sixty-north.com/c/t.txt
def fetch_words(url):
    """Fetch a list of words from the URL.
    
    Args:
        url : The URL of a UTF-8 text document
    
    Returns:
        A list of strings containing the words from the document.  
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    return story_words


def print_items(items):
    """Prins one item per line.
    
    Args:
        items : An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Prints each word from a text document from a URL
    
    Args:
        url : The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


# sys.argv[1]  represents the command line argument like while executing the module below:
# python words.py        
if(__name__=="__main__"):
    main(sys.argv[1])  #The 0th argument of sys.argv is the module filename. So, we use 1st argument.