import json
import sys
import os
import playsound
from pathlib import Path

from recorder import live_speech

playsound.playsound(Path(__file__).parent / "sounds" / "bootup.mp3")

def detect_wakeup(command: str, wakeup_words: list[str]):
    command = command.lower()

    for word in wakeup_words:
        word = word.lower()
        if word in command:
            return True
        
    return False

if not os.path.exists("wakeup_words.json"):
    print("You must run init.py first!")
    sys.exit(1)

with open("wakeup_words.json", "r") as f:
    wakeup_words = json.load(f)

while True:
    for message in live_speech():
        if detect_wakeup(message, wakeup_words):
            print(f"Detected: {message}")
            playsound.playsound(Path(__file__).parent / "sounds" / "detected.mp3")
            break
    for message in live_speech(50):
        print (f"Command: {message}")
        break
