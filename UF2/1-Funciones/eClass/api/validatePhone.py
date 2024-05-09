import requests
number = '+34656111111'
api_url = 'https://api.api-ninjas.com/v1/validatephone?number={}'.format(number)
response = requests.get(api_url, headers={'X-Api-Key': 'oGl6knmWFXLHRXXhT+iWig==Is0sEoStwrbNQGkt'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)