import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 4444
    result = s.connect_ex((host,port))
    print('Result is {}'.format(result))
    s.close()

if __name__ =='__main__':main()