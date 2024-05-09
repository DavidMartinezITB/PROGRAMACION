"""
David Martinez - ASIXc1A
"""

import os, requests, json

PLAYAS = {}

def getJson():
    data = requests.get('https://opendata-ajuntament.barcelona.cat/data/dataset/953a7e5e-e238-417f-b21d-232447c164cb/resource/50cadf75-c52e-44c6-ba5a-a387c968258b/download')
    data = json.dumps(json.loads(data.content))

    f = open('data.json', 'wt', encoding='UTF-8')
    f.write(data)
    f.close()

def loadData():
    with open('data.json', 'r') as f:
        data = json.loads(f.read())
        
        for playa in data:
            district = playa['addresses'][0]['district_name']
            if district not in PLAYAS:
                PLAYAS[district] = []
            PLAYAS[district].append(playa['name'])

def main():
    if 'data.json' not in os.listdir('.'):
        getJson()
    
    loadData()
    for i in PLAYAS:
        print(i, len(PLAYAS[i]), sep='\t')
    
if __name__ == '__main__':
    main()