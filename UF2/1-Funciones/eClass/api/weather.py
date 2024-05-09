import requests, json

API_KEY = 'oGl6knmWFXLHRXXhT+iWig==Is0sEoStwrbNQGkt'

CITY = 'Barcelona'
api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(CITY)
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
if response.status_code == requests.codes.ok:
    dades = json.loads(response.text)
    print('A {} fa {} graus'.format(CITY, dades['temp']))
else:
    print("Error:", response.status_code, response.text)