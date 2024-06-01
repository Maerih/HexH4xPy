# Author: Onyonka Maeri
# Date: 2024-06-01
# WARNING:
# This script is intended for educational purposes only.
# Unauthorized use of this script on systems you do not own or
# have explicit permission to test is illegal and unethical.
# Use responsibly and within the bounds of all applicable laws.

import socket

def banner(ip,port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(15)
    print(s.recv(1024))

def main():
    ip = input("Please Enter IP: ")
    port = str(input("\nPlease Enter Port:"))
    banner(ip,port)

if __name__ =='__main__':main()