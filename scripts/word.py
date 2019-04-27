from urllib.request import urlopen
import sys
"""
This is word script that take inputs and return the
text from the url
Usage: 
    <script> url
"""
def fetch_words(url):
    """
    This is function takes the text url as input and reads
    its content and return the words of the text file.
    Usage:
        script.fetch_words( url )
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_words(items):
    """
    This function reads items and print them

    :param items:
    :return:
    """
    for item in items:
        print(item)

def main(url):
    """
    This function takes the url supplied in argument by end user
    and fetch the content of the text url
    and using the print_words function it displays those contents.

    :param url:
    :return:
    """
    words = fetch_words(url)
    print_words(words)

if __name__ == '__main__' :
    """
    This is the first condition which read the module name
    and triggers the main condition.
    
    """
    main(sys.argv[1])
