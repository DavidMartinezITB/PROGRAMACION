import logger

# Retorna una lista con las lineas de un fichero
def getDataFromFile(fileName):
    try:
        with open(fileName, 'r') as f:
            lines = f.readlines()
        logger.info(f'Retrieved data from {fileName}!')
        return lines
    except:
        logger.error(f'Cannot open {fileName}!')
        return []

# Elimina los saltos de linea en caso de que los haya
def cleanLines(lines):
    nLines = []
    for line in lines:
        if line.endswith('\n'):
            nLines.append(line[:-1])
        else:
            nLines.append(line)
    return nLines

# Agrega saltos de linea en caso de que no los haya (no lo agrega en la ultima fila)
def formatLines(lines):
    nLines = []
    for line in lines[:-1]:
        if not line.endswith('\n'):
            nLines.append(line + '\n')
    nLines.append(lines[-1])
    return nLines