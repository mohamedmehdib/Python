import requests
import pprint
           
API_KEY = "4c7fb5ed8bbb488d8c620babd7a690d3"

country = input("Enter the code of ur country ( code of two lettre ) : ")

request = requests.get(f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}").json()

news = request["articles"]

for new in news:
    print()
    if new["author"]=="" or not(new["author"]):
        print("Author : Anonymous")
    else:
        print(f'Author : {new["author"]}')

    print(f'The description : {new["description"]}\n')
    print(f'By : {new["source"]["name"]}\n')
    print(f'Do you want to read more ? This is the url of the new : {new["url"]}\n')




    print("*"*80)

