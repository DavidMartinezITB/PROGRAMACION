# Extracto de la ultima fase del proyecto 'ParaulesBoges'
def getFiles(DIRECTORI):
    contenido = os.listdir(DIRECTORI)

    for elemento in contenido:
        ruta_elemento = os.path.join(DIRECTORI, elemento)

        if os.path.isdir(ruta_elemento):
            getFiles(ruta_elemento)
        elif ruta_elemento.endswith('.txt'):
            rawFiles.append(ruta_elemento)