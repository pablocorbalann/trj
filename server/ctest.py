# client connection test from the server side
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.1.1', 4444))

while True:
    s.send(input('> ').encode('utf-8'))
    msg = s.recv(512).decode('utf-8')
    print(msg)
