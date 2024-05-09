import os

DIR = '.'
OUT_DIR = 'picturesClosed'
files = []

def directoryExists(dir):
    return os.path.exists(dir)

def mkdir(dir):
    os.makedirs(dir)

def getFiles(directorio):
   contenido = os.listdir(directorio)

   for elemento in contenido:
       ruta_elemento = os.path.join(directorio, elemento)

       if os.path.isdir(ruta_elemento):
           getFiles(ruta_elemento)
       elif ruta_elemento.endswith('.in'):
           files.append(ruta_elemento)

def openEyes(file):
    with open(file, 'r') as f:
        data = f.read().replace('0', '-')
    writeOutput(file, data)

def openFiles():
    for file in files:
        openEyes(file)

def writeOutput(file, data):
    fileName = os.path.splitext(file)[0]
    outFile = f'{fileName}.out'.replace('./pictures/', f'./{OUT_DIR}/')
    with open(outFile, 'w') as f:
        f.write(data)

def main():
    getFiles(DIR)
    if files:
        if not directoryExists(OUT_DIR):
            mkdir(OUT_DIR)
        openFiles()

if __name__ == '__main__':
    main()