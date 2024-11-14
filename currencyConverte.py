import requests
import pprint

url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_aDuAq4be29RdV04rTgxpNTeYDfXha1IdAFcXvST9"

data = requests.get(url).json()

available = []

for key,val in data["data"].items():
    available.append(key)

# pprint.pprint(data)

while True:
    print("Valid currencies : ")
    for currency in available:
        print(currency, end=" | ")
    print("\nPlease enter valid currencies")
    From = input("You want to convert from ? : ")
    To = input("To ? : ")
    if To in available and From in available:
        break

res = data["data"][To] / data["data"][From]

print(f"{From} = {res:.3f} {To}")

