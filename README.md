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
1. Open Command Prompt and navigate to the project folder  
2. Activate the virtual environment:  
   venv\Scripts\activate  
3. Run the script:  
   python keylogger.py  
4. The script will begin logging keystrokes and capturing screenshots every 10 seconds  
5. To stop the script, press:  
   Ctrl + C


## Note
All logs and screenshots are excluded from version control using `.gitignore` for privacy and security reasons.

