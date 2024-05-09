import xmltodict

FILE = 'data.xml'

def getXmlContent(file):
    with open(file, 'r') as f:
        return xmltodict.parse(f.read())

data = getXmlContent(FILE)

for dia in data['root']['prediccion']['dia']:
    fecha = dia['@fecha']
    prob = dia['prob_precipitacion']
    print(fecha, prob)