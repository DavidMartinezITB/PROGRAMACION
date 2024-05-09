import requests

api_url = 'https://api.api-ninjas.com/v1/webscraper?url=https://gencat.cat?text_only=true?user_agent=Mozilla/5.0%20(Windows NT 6.1;%20Win64;%20x64;%20rv:47.0)%20Gecko/20100101%20Firefox/47.0'
response = requests.get(api_url, headers={'X-Api-Key': 'oGl6knmWFXLHRXXhT+iWig==Is0sEoStwrbNQGkt'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)