import json, logger

CFG_FILE = 'config.json'

def getConfigFromJson():
    try:
        with open(CFG_FILE, 'r') as f:
            return json.loads(f.read())
    except Exception as e:
        print(f'CRITIC: Cannot load config from {CFG_FILE}!')
        print(e)