# -----------  Importations ---------

from random import randint
from numpy import array

# -----------  Variables ------------

words=["apple","microsoft","google","meta"]

hangman = [
    "",
    "o",
    " o\n |",
    " o\n/|",
    " o\n/|\ ",
    " o\n/|\ \n/ ",
    " o\n/|\ \n/ \ "
]

random = randint(0,len(words)-1)

word=words[random]

t=array([str()]*len(word))

# -----------  PP -------------------

for i in range(len(word)):
    t[i]="_"


def complete(text):
    ok=True
    i=0
    while ok and i<len(text):
        if text[i]=="*":
            i=i+1
        else:
            ok=False
    return ok


def game(word,hangman):
    faux=0
    while faux<6:
        lettre=input("Donner une lettre : ")
        j=word.find(lettre)
        if lettre in word:
            word=word.replace(lettre,"*",1)
            t[j]=lettre
            print("\n")
            print(hangman[faux])
        else:
            faux+=1
            print("\n")
            print(hangman[faux])

        print("\n")
        for i in range(len(word)):
            print(t[i],end=" ")
        print("\n\n")

        if complete(word):
            faux=6
        


        print("\n***********************\n\n")

    if complete(word):
        print("\n\nCongratulations !!! You Won\n\n")
    else:
        print("\n\nGame Over !!! You Lost\n\n")
    




game(word,hangman)