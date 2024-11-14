import time


def wpm():
    p = "The sun sets, casting a warm glow across the lake. Water ripples gently, reflecting the sky's colors. Families gather around campfires, toasting marshmallows. Stars emerge, painting the night sky."
    nWord = 29
    begin = time.time()
    print(p)
    ans = input("\nAppuyez sur Entrée pour arrêter le calcul du temps ! \n")

    print(ans)
    finish = time.time()
    duration = (finish - begin)/60
    speed = nWord / duration

    if speed>40:  
        print(f"Your speed is {speed} , You're amazing !")
    elif speed>30:
        print(f"Your speed is {speed} , You're a rapid person !")
    else:
        print(f"Your speed is {speed} , You can do better !")


wpm()