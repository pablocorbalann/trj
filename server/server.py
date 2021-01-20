import socket
import threading

import monoclient

class Server:
    """
    This class is used to manage all the servers trj uses and to manage
    the sockets.
    """
    def __init__(self, port, conf):
        """
        This is the constructor method for the Server class, from here all the
        attributes of the class are created

        Parameters:
            port => The port the server should connect to
            conf => A tuple containing the configuration of the server
                (
                    server ip,
                    server decode format,
                    server max bites
                )
        """
        self.port = port
        self.ip = conf[0]
        self.dcf = conf[1] # dcf = DeCode-Format
        self.bites = conf[2]

        self.addr = (self.ip, self.port)

        self.disconnect = "!DISCONNECT" # msg to disconnect

        # create the actual server of the instance
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.addr) # bind the server to the addr

        self.clients = [] # stores configuration of each client

    def handle_client(self, client_id, conf):
        """
        This method is a thread used to handle all the clients that connect to
        the server.

        Parameters
        ----------
        client_id: int
            the number to determine the client
        conf: monoclient.ClientConfiguration
            The configuration of the client
        """
        client = monoclient.Client(client_id, conf)
        # some debug from the server
        print(f"[NEW CONNECTION] {client.conf.addr} connected.")
        # append the connection to the clients
        self.clients.append(client)
        connected = True # 1 if the client is still connected
        while connected:
            client.send(input(">>> "), self.dcf)
            client_data = client.recv(self.bites, self.dcf)
            print(f"{client.conf.__repr__()}: {client_data}")

    def start(self):
        """
        This method is used to start the server itself using the .listen() method
        and then starting a while loop to create the threads

        Parameters:
            self => The Server() class
        """
        # start the server and listen it
        self.server.listen()
        print(f"[LISTENING]: Server is listening on {self.addr}")
        running = True
        client_counter = 0
        while running:
            try:
                client_counter += 1
                conn, addr = self.server.accept()
                client_configuration = monoclient.ClientConfiguration(conn, addr)
                # create the thread for the self.handle_client method
                thread = threading.Thread(target=self.handle_client, args=(client_counter, client_configuration))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {len(self.clients) + 1}")
            except Exception as e:
                # report the bug informing the user
                print(f"[SERVER CRASH]: Fatal error, {e}")
                running = False

if __name__ == '__main__':
    # actually run the server
    sconf = [
        socket.gethostbyname(socket.gethostname()), 
        "utf-8",
        128
    ]
    s = Server(8080, sconf)
    s.start()
