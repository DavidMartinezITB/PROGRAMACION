import os, config

def fileExists():
    return os.path.exists(config.FILE)

def writeInFile(fileName, content):
    try:
        with open(fileName, 'w') as f:
            f.write(content)
    except:
        print('Error al escribir en fichero!')