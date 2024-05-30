import socket

class Grabber:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.socket.settimeout(0.3)
        self.socket.connect((self.ip, self.port))

    def read(self,length=1024):
        return self.socket.recv(length)
    
    def close(self):
        self.socket.close()

def main():
    grabber = Grabber('62.8.88.45', 443)
    print(grabber.read())
    grabber.close()

if __name__ =='__main__':main()