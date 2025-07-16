# Keylogger with Screenshot Capture

This project was developed as part of the Cantilever Cybersecurity Internship (Task 2).

It demonstrates how keylogging and periodic screen capture can be performed using Python. The project is intended for educational purposes only.

## Features
- Logs all keyboard input to a text file
- Captures desktop screenshots every 10 seconds
- Stores all data in a timestamped folder
- Uses multithreading for concurrent logging and screenshot capture
- Cleanly stops execution using Ctrl + C

## Technologies Used
- Python 3.13
- pynput
- pyautogui
- threading
- datetime
- time
- os

## How to Run
1. Open terminal and activate your Python environment
2. Run the script:
3. The script will log keystrokes to `keystrokes.txt` and save screenshots
4. Press `Ctrl + C` to stop the script

## Note
All logs and screenshots are excluded from version control using `.gitignore` for privacy and security reasons.

