"""
This super small testing file, contains a super small
example of a working socket that acts like a server in python.
The file is not really usefull.

For more information: github.com/pablocorbalann/trj
"""
import socket

addr = ("0.0.0.0", 8080)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

conn, addr = server.accept()

while True:
    message = conn.recv(128).decode("utf-8")
    print(f"MESSAGE: {message}")
