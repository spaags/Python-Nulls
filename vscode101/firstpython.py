try:
    import time
except ImportError:
    import os
    os.system('pip install time')
    import time

try:
    import keyboard
except ImportError:
    import os
    os.system('pip install keyboard')
    import keyboard

def keyPressed(key):
    if key.name == 'a':
        keyboard.release('d')
    elif key.name == 'd':
        keyboard.release('a')

keyboard.on_press(keyPressed)

while True:
    time.sleep(1)