import crafter, data, file, config

def main():
    if file.fileExists():
        data.getDataFromFile()
    data.getDataFromKeyboard()

    shortest = crafter.getShortestBook()
    longest = crafter.getLongestBook()
    amount = len(data.data)

    fileContent = crafter.craftFileContent(shortest, longest, amount)
    file.writeInFile(config.FILE, fileContent)

if __name__ == '__main__':
    main()