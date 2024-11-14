inp="""***************************

What do you want !
1. Aad a book !
2. Borrow a book !
3. Return a book !

***************************

Choose : """


import json

class Book:
    def __init__(self,title,is_avaible=False,borrower=None):
        self.title = title
        self.is_avaible = is_avaible
        self.borrower = borrower

    def addBook():
        book_title = input("Enter book name: ")
        with open("books.json", "r") as file:
            data = json.load(file)

        data.append({
            "title": book_title,
            "is_avaible": True,
            "Borrower": None
        })

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

        print("The book is added !")

    def returnBook():
        borrower_name=input("Enter borrower name: ")
        with open("borrowers.json", "r") as file:
            dataBorrowers = json.load(file)

        with open("books.json", "r") as file:
            dataBooks = json.load(file)
        verif=False
        i=0
        while i<len(dataBorrowers) and not(verif):
            if(dataBorrowers[i]["name"]==borrower_name):
                verif=True
                index=i
            else:
                i+=1

        if verif:

            dataBooks[index]["is_avaible"]=True
            dataBooks[index]["Borrower"]=None
            with open("books.json", "w") as file:
                json.dump(dataBooks, file, indent=4)

            dataBorrowers.remove(dataBorrowers[index])    
            
            with open("borrowers.json", "w") as file:
                json.dump(dataBorrowers, file, indent=4)

            print(f"{borrower_name} return the book of : ")







        else:
            print(f"There are not a borrower with name of {borrower_name} !")




class Borrower:
    def __init__(self,name,title=None):
        self.name = name
        self.title = title

    def setName(self,name):
        self.name = name


    def addBorrower():

        borrower_name = input("Enter borrower name: ")
        title = input("Enter which title he borrow: ")
        with open("borrowers.json", "r") as file:
            dataBorrowers = json.load(file)

        dataBorrowers.append({
            "name": borrower_name,
            "title": title
        })

        
        with open("books.json", "r") as file:
            dataBooks = json.load(file)
        
        verif=False
        i=0

        while i<len(dataBooks) and not(verif):
            if (dataBooks[i]["title"]==title):
                verif=True
                indexBook = i
            else:
                i+=1

        if verif:
            if dataBooks[indexBook]["is_avaible"]==True:
                print("You borrow this book !")
                with open("borrowers.json", "w") as file:
                    json.dump(dataBorrowers, file, indent=4)

                dataBooks[indexBook]["is_avaible"]=False
                dataBooks[indexBook]["Borrower"]=borrower_name
                



                with open("books.json", "w") as file:
                    json.dump(dataBooks, file, indent=4)

                
                

            else:
                print(f"I'm sorry the book is borrowed by \"{dataBooks[indexBook]['Borrower']}\"")
        else:
            print("It doesn't exist this book ! Do you want to add it ?")

        



choice=int(input(inp))

while choice not in [1,2,3]:
    choice=int(input(inp))
    

if choice==1:
    Book.addBook()
elif choice==2:
    Borrower.addBorrower()
else:
    Book.returnBook()

