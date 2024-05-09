import os

DIRECTORI_ENTRADA = "entrada"
DIRECTORI_SORTIDA = "sortida"

INPUT_FILE = 'paraules.txt'
OUTPUT_FILE = 'paraules_boges.txt'

LOG_DIRECTORY = 'log'
LOG_FILE = 'boges.log'
LOG_PATH = os.path.join(LOG_DIRECTORY,LOG_FILE)

LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
LOG_MODE = 'a'