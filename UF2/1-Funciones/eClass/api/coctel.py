import requests

name = 'bloody mary'
api_url = 'https://api.api-ninjas.com/v1/cocktail?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'oGl6knmWFXLHRXXhT+iWig==Is0sEoStwrbNQGkt'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)