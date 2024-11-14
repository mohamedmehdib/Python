import clipboard
import json

SAVED_DATA = "clipboard/clipboard.json"

while True:
    choice = int(input("Copy or paste ? (1 for copy and 2 for paste) : "))
    if choice in [1,2] :
        break

if choice == 1 :
    print("Avaible data to copy !")
    with open(SAVED_DATA,"r") as file:
        data = json.load(file)
    for value in data:
        for val,key in value.items():
            print(f"{val} : {key}")
    while True:
        value = int(input("Which data do you want to copy ? ( Enter the index ) : "))
        if value<=len(data):
            clipboard.copy(data[value-1][str(value)])
            print("Data copied to the clipboard !")
            break

else:
    with open(SAVED_DATA,"r") as file:
        data = json.load(file)
    
    data.append({
        f"{len(data)+1}":clipboard.paste()
    })

    with open(SAVED_DATA,"w") as file:
        json.dump(data,file,indent=4)

    print("Data saved !")

