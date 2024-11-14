from pynput import keyboard
import mouseMovingBot

target_word = "hello"
typed_word = ""
word_count = 0

def on_press(key):
    global typed_word, word_count
    try:
        if key.char:
            typed_word += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            typed_word += ' '
        elif key == keyboard.Key.enter:
            typed_word = ''


    if typed_word.strip() == target_word:
        word_count += 1
        with open("wordCounter.txt", "w") as file:
            file.write(f"{target_word} : {word_count}")
        
        mouseMovingBot.mouseMoving() 
        typed_word = ''

def on_release(key):
    if key == keyboard.Key.esc:
        return False 

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
