from pynput.mouse import Button, Controller
import time
mouse = Controller()

from pynput import keyboard

def on_press(key):
    while True:
        mouse.click(Button.left, 1)
        time.sleep(1)
        if key == keyboard.Key.esc:
            break


def on_release(key):
    if key == keyboard.Key.shift_r:
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
