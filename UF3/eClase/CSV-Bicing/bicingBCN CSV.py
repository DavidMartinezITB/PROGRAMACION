import csv

fitxer='2023_03_Marc_BicingNou_INFORMACIO.csv'

try:
    maxim=0
    station_id=0
    name=''
    lista_id=[]
    contador=0
    data = csv.DictReader(open(fitxer, newline=''))

    for row in data:
        capacitat= row['capacity']
        if row['station_id'] not in lista_id:
            lista_id.append(row['station_id'])
            contador+=int(row['capacity'])

        if int(capacitat)>maxim:
            maxim=int(capacitat)
            station_id=row['station_id']
            name=row['name']

    print(maxim, station_id, name)
    print(len(lista_id))
    print(contador)

except FileNotFoundError:
    print('no >:C')