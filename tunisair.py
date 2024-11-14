import requests
import pprint



KEY = 'f021da9d79c170f8d73ad1f4943541e3'
url = f"https://api.aviationstack.com/v1/airports?access_key={KEY}"

response = requests.get(url).json()

l = len(response['data'])

for i in range(l):
    if response['data'][i]['country_name'] == "France":
        pprint.pprint(response['data'][i])