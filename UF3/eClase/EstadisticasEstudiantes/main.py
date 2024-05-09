def getFile():
    fileName = input()
    if len(fileName.split()) != 1:
        return False
    # TODO: Validar que el fichero existe y tiene el formato correcto

    return fileName

def getData(file):
    notas = []
    try:
        with open(file, 'rt') as f:
            for i in f.read().split():
                try:
                    notas.append(int(i))
                except:
                    pass
    except FileNotFoundError:
        print('El fichero no existe!')
    return notas

def ordenarLista(list):
    return sorted(list)

def obtenerMedia(list):
    acc = 0
    for i in list:
        acc += i
    return acc / len(list)

def main():
    notas = getData(getFile())
    print(notas)
    if len(notas) != 0:
        notas = ordenarLista(notas)
        print("Nota minima:\t{}".format(notas[0]))
        print("Nota maxima:\t{}".format(notas[-1]))
        print("Nota media:\t{}".format(obtenerMedia(notas)))

if __name__ == '__main__':
    main()