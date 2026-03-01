import threading
import time

from pynput.keyboard import KeyCode, Listener
from pynput.mouse import Button, Controller

TOGGLE_KEY = KeyCode(char="2")

toggled = False
mouse = Controller()


def clicker():
    while True:
        if not toggled:
            mouse.click(Button.left, 1)
            time.sleep(0.01)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global toggled
        toggled = not toggled


t1 = threading.Thread(target=clicker)
t1.start()

# ...or, in a non-blocking fashion:
listener = Listener(on_press=toggle_event)
listener.start()
