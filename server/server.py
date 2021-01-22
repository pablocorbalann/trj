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

        self.clients = {} # stores configuration of each client


    def loop_client(self, client):
        """
        Sends messages and receives messages from an specific client.

        Parameters
        ----------
        client: monoclient.Client
            The client to iterate
        """
        command = input("> ")
        # send the actual command.
        client.send(command, self.dcf)
        client_data = client.recv(self.bites, self.dcf)
        # debug the client data
        print(f"{client.conf.__repr__()}: {client_data}")
        # store the command
        comand_data = monoclient.Command(command, client_data)
        self.clients[client.client_id].commands.append(commands_data)
   

    def send_to_all_clients(self):
        """
        Request a command and sends that command to all the clients connected

        (kind of a broadcast)
        """
        command = input("> ")
        client_data_registrer = []
        for i, client in self.clients.items():
            client.send(command, self.dcf)
            client_data = client.recv(self.bites, self.dcf)
            client_data_registrer.append(client_data)
        print(f"{command} sended to {len(client_data_register)} clients")


    def loop(self):
        """
        This method is used to loop the options and depending on what the
        server manager types, it will invoke other methods.
        """
        looping = True
        # create the simple hash
        loop_hash = {
            1: self.send_to_all_clients
        }
        while looping:
            option = 0
            print(f"[1]: Send a command to all the clients ({len(self.clients)})")
            try:
                option = int(input("Select what do you want to do: "))
            except Exception as e:
                print("Error, invalid iteral / option...")
            try:
                loop_hash[option]()
            except KeyError as e:
                print("Invalid option... {option}")
            except Exception as e:
                print("Internal crash at looping options...")


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
        self.clients[client_id] = client

    def start(self):
        """
        This method is used to start the server itself using the .listen() method
        and then starting a while loop to create the threads

        Parameters: self => The Server() class
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
                print(f"[ACTIVE CONNECTIONS] {len(self.clients)}")
                self.loop()
            except Exception as e:
                # report the bug informing the user
                print(f"[SERVER CRASH]: Fatal error, {e}")

if __name__ == '__main__':
    # actually run the server
    sconf = [
        socket.gethostbyname(socket.gethostname()), 
        "utf-8",
        128
    ]
    s = Server(8080, sconf)
    s.start()
