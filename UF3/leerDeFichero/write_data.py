import logger

# data = lista con las lineas
# Las lineas deben acabar en \n, si queremos salto de linea:
#   ['asdfg\n', '\n', '\n', '\n', 'hhhh']
def writeInFile(fileName, data=[]):
    print(data)
    if data == []:
        logger.warning(f'Nothing to write in {fileName}...')
        return
    try:
        with open(fileName, 'w') as f:
            f.write("".join([str(elem) for elem in data]))
    except:
        logger.error(f'Cannot open {fileName}!')