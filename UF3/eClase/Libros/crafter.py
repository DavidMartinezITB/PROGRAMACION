import data, config

def getLongestBook():
    longest = 0
    longestIndex = 0
    for i in range(len(data.data)):
        if data.data[i][2] > longest:
            longest = data.data[i][2]
            longestIndex = i
    return longestIndex

def getShortestBook():
    shortest = data.data[0][2]
    shortestIndex = 0
    for i in range(len(data.data)):
        if data.data[i][2] < shortest:
            shortest = data.data[i][2]
            shortestIndex = i
    return shortestIndex

def craftBookData(book):
    return f"{book[0]} - {book[1]} - {book[2]} {config.PAGE_LABEL}\n"

def craftFileContent(shortest, longest, amount):
    books = '\n'
    for book in data.data:
        book = craftBookData(book)
        books += book

    return f"Llibres\n{config.SEP}{books}{config.SEP}\nTotal: {amount} llibres\nLlibre més curt: {craftBookData(data.data[shortest])}Llibre més llarg: {craftBookData(data.data[longest])}"
