# _____________ Importations ________________
from numpy import array

# _____________   Variables   _______________

one=["0","1","2"]
two=["3","4","5"]
three=["6","7","8"]
role="O"

win=[
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]
x=[]
o=[]
# __________________ PP ______________________


def refresh():
    for i in range(3):
        print(one[i],end="   ")
    print("\n")
    for i in range(3):
        print(two[i],end="   ")
    print("\n")
    for i in range(3):
        print(three[i],end="   ")
    print("\n")


def testWin(role,win):
    check=False
    i=0
    while i<len(win) and not(check):
        if ((win[i])[0] in role) and ((win[i])[1] in role) and ((win[i])[2] in role) :
            check=True
        i+=1
    return check


def play(role):
    i=0
    while(i<9):
        if role=="X":
            role="O"
            print("It's role of "+role+"\n")
            refresh()
            index=int(input("Indicate the index you want : "))
            if(0<=index<=2):
                one[index]="O"
            if(3<=index<=5):
                two[index-3]="O"
            if(6<=index<=8):
                three[index-6]="O"
            o.append(int(index))
            print(o)
        else:
            role="X"
            print("It's role of "+role+"\n")
            refresh()
            index=int(input("Indicate the index you want : "))
            if(0<=index<=2):
                one[index]="X"
            if(3<=index<=5):
                two[index-3]="X"
            if(6<=index<=8):
                three[index-6]="X"
            x.append(int(index))
            print(x)

        if testWin(x,win):
            print("\n----------------------------\n")
            print("\nX win !\n")
            i=9
        elif testWin(o,win):
            print("\n----------------------------\n")
            print("\nO win !\n")
            i=9

            
        print("\n----------------------------\n")
        i+=1
        

play(role)