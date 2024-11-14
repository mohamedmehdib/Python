import pyautogui as pag
import random
import time

def mouseMoving():
    start_time = time.time()
    while time.time() - start_time < 10:
        x = random.randint(0, 1200)
        y = random.randint(0, 900)
        pag.moveTo(x, y, 0.1)
        time.sleep(0.1)
    print("Mouse movement finished.")

if __name__ =="__main__":
    mouseMoving()

