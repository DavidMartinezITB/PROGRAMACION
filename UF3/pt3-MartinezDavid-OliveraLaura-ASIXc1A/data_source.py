import logging, os

rawFiles = []
files = []

def get_dir_content(DIRECTORI):
    getFiles(DIRECTORI)
    for file in rawFiles:
        files.append(file[len(DIRECTORI) + 1:])
    
    return files

def getFiles(DIRECTORI):
    contenido = os.listdir(DIRECTORI)

    for elemento in contenido:
        ruta_elemento = os.path.join(DIRECTORI, elemento)

        if os.path.isdir(ruta_elemento):
            getFiles(ruta_elemento)
        elif ruta_elemento.endswith('.txt'):
            rawFiles.append(ruta_elemento)


def get_file_path(DIRECTORI_ENTRADA, DIRECTORI_SORTIDA, fitxer):
    nom_fitxer=fitxer[:-4]
    fitxer_sortida=os.path.join(DIRECTORI_SORTIDA, f'{nom_fitxer}_boges.txt')
    ruta_fitxer = os.path.join(DIRECTORI_ENTRADA, fitxer)
    logging.info(f'PROCESSING: {ruta_fitxer}')
    return fitxer_sortida, ruta_fitxer