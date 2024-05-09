import config

data = []

def getDataFromFile():
    with open(config.FILE, 'tr') as f:
        lines = f.readlines()
        for i in range(2, len(lines) - 4):  
            bookData = lines[i].replace('\n', '').split(' - ')
            bookData[2] = int(bookData[2].split()[0])
            data.append(tuple(bookData))

def getDataFromKeyboard():
    n = 0
    while n <= 0:
        try:
            n = int(input('No. de libros: '))
        except:
            pass
    for i in range(n):
        titulo = ''
        while titulo == '':
            titulo = input('Titulo: ')

        autor = ''
        while autor == '':
            autor = input('Autor: ')

        pags = 0
        while pags <= 0:
            try:
                pags = int(input('No. de paginas: '))
            except:
                pass
        
        data.append((titulo, autor, pags))