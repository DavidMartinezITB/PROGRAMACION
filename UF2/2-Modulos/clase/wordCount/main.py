import wordCount

def main():
    text = input()
    wordCount.printFormattedDict(wordCount.getWordCount(wordCount.cleanText(text)))

if __name__ == '__main__':
    main()