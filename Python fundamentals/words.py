import sys
from urllib.request import urlopen


#  url == http://sixty-north.com/c/t.txt
def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    return story_words

def print_items(items):
    for item in items:
        print(item)

def main(url):
    words = fetch_words(url)
    print_items(words)


# sys.argv[1]  represents the command line argument like while executing the module below:
# python words.py http://sixty-north.com/c/t.txt     
if(__name__=="__main__"):
    main(sys.argv[1])