translate = {
    "A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-",
    "L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-",
    "W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":"-----",
    "6":"-....","7":"--...","8":"---..","9":"----."," ":"/"
}

textInput = "Input your text !"
codeInput = "Input your code !"

while True:
    choise = int(input("What do you want ? (1: from text to code , 2: from code to text) : "))
    if choise in [1,2]:
        break

    
if choise==1:
    text = input("Enter your text : ")
    code = ""
    for i in range(len(text)):
        lettre = text[i].upper()
        code += translate[lettre]+" "

    print(f"Your code is : {code}")


else :
    code = input("Enter your code : ")+" "
    text = ""
    count = code.count(" ")
    for i in range(count):
        p = code.find(" ")
        lettre = code[:p]
        for key, val in translate.items():
            if val == lettre:
                text += key.lower()
        code = code[p+1:]

    print(f"Your text is : {text.capitalize()}")