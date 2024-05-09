import collections


def cleanText(text):
    BAD_CHARS = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    ntext = ''
    text = text.lower()

    # Delete starting or ending apostrophe chars
    for word in text.split():
        while word.startswith("'"):
            word = word[1:]
        while word.endswith("'"):
            word = word[:-1]
        ntext += word + ' '

    # Delete all badchars except apostrophe
    for char in BAD_CHARS:
        ntext = ntext.replace(char, ' ')
    
    return ntext

def getWordCount(text):
    counters = {}
    for word in text.split():
        if not word in counters: # If not exists in dict
            counters[word] = 1
        else:
            counters[word] += 1
    
    # Ordering dict
    counters = collections.OrderedDict(sorted(counters.items()))
    
    return counters

def printFormattedDict(dict):
    # Prints a formatted version of a dict (key: value)
    for i in dict:
        print(i, dict[i], sep=': ')