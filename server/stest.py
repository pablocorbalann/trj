import socket

addr = ("0.0.0.0", 8080)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

conn, addr = server.accept()

while True:
    message = conn.recv(128).decode("utf-8")
    print(f"MESSAGE: {message}")
