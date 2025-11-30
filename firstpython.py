import keyboard
import time

def keyPressed(key):
    if key.name == 'a':
        keyboard.release('d')
    elif key.name == 'd':
        keyboard.release('a')

keyboard.on_press(keyPressed)

while True:
    time.sleep(1)