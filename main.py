import string
import time
from pynput.keyboard import Controller, Key, Listener

keyboard = Controller()
running = False


def auto_type():
    letters = string.ascii_lowercase

    while running:
        for char in letters:
            if not running:
                break
            keyboard.press(char)
            keyboard.release(char)


def on_press(key):
    global running
    if key == Key.f8:
        running = not running
        if running:
            import threading
            threading.Thread(target=auto_type, daemon=True).start()


def main():
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
