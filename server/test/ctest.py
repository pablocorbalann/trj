"""
This super small testing file has been developed for testing the
connection of an specific client from the server side, it's 
like an endless looping that receives the information of the client
and prints it. It's not an usefull file.

For more information: github.com/pablocorbalann/trj
"""
# client connection test from the server side
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080))

while True:
    # s.send(input('> ').encode('utf-8'))
    msg = s.recv(512).decode('utf-8')
    print(msg)
