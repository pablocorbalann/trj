import socket
import threading
import sys

import monoclient
import decorators

def print_server_options(options):
    """
    This function is used to print the server options using a format. It uses
    a parameter :param options: that has the form of:

        {
            1: (function_1, message1),
            2: (function_2, message2),
            ...
            n: (function_n, messagen)
        }

    And prints it like:
        
        [1] message1
        [2] message2
        [n] message3
    """
    colors = decorators.Colors()
    print(f"{colors.INFO}[0]{colors.ENDC} Close the server...")
    for i, option in options.items():
        print(f"{colors.INFO}[{i}]{colors.ENDC} {option[1]}")

def request_server_option():
    """
    Is used to request the option and prints it.

    Returns
    -------
    option: int
        The option that has to be returned
    """
    colors = decorators.Colors()
    option = 0
    try:
        option = int(input(f"{colors.OK}Select what do you want to do: {colors.ENDC}"))
    except ValueError as e:
        print(f"{colors.ERR}Error, invalid value for base 10 {e}{self.__colors.ENDC}")
    except Exception as e:
        print(f"{colors.ERR}Error, invalid iteral / option... {e}{colors.ENDC}")
    return option


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
        self.__loop_thread = None

        self.disconnect = "!DISCONNECT" # msg to disconnect

        # create the actual server of the instance
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.addr) # bind the server to the addr

        self.clients = {} # stores configuration of each client

        # colors
        self.__colors = decorators.Colors()


    def loop_client(self, client):
        """
        Sends messages and receives messages from an specific client.

        Parameters
        ----------
        client: monoclient.Client
            The client to iterate
        """
        command = input(">>> ")
        # send the actual command.
        client.send(command, self.dcf)
        client_data = client.recv(self.bites, self.dcf)
        # debug the client data
        print(f"{self.__colors.INFO}{client.conf.__repr__()}: {client_data}{self.__colors.ENDC}")
        # store the command
        comand_data = monoclient.Command(command, client_data)
        self.clients[client.client_id].commands.append(commands_data)
   

    def __send_to_all_clients(self):
        """
        Request a command and sends that command to all the clients connected

        (kind of a broadcast)
        """
        command = input(">>> ")
        cdr = [] # client data register
        for i, client in self.clients.items():
            client.send(command, self.dcf)
            client_data = client.recv(self.bites, self.dcf)
            cdr.append(client_data)
        print(f"{self.__colors.INFO}{command} sended to {len(cdr)} clients{self.__colors.ENDC}")


    def __loop(self):
        """
        This method is used to loop the options and depending on what the
        server manager types, it will invoke other methods.
        """
        looping = True
        # create the simple hash
        loop_hash = {
            1: (self.__send_to_all_clients, "Send a message to all the clients")
        }
        while looping:
            option = 0
            # Print the options
            print_server_options(loop_hash)
            option = request_server_option()
            # Get the option and start the hash map 
            try:
                loop_hash[option][0]() # the position 0 is the function
            except KeyError as e:
                print(f"{self.__colors.ERR}Invalid option... {option}{self.__colors.ENDC}")
            except Exception as e:
                print(f"{self.__colors.FAIL}Internal crash at looping options... {e}{self.__colors.ENDC}")


    def __handle_client(self, client_id, conf):
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
        print(f"{self.__colors.INFO}[NEW CONNECTION] {client.conf.addr} connected.{self.__colors.ENDC}")
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
                thread = threading.Thread(target=self.__handle_client, args=[client_counter, client_configuration])
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {len(self.clients)}")
                # check if the loop thread is already working, if it's restart it.
                decorators.update_server_connections(self.addr, len(self.clients))
                if self.__loop_thread != None:
                    self.__loop_thread.join()
                    self.__loop_thread = None
                self.__loop_thread = threading.Thread(target=self.__loop)
                self.__loop_thread.start()
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
    # check if the user did python3 server.py <ip> <port>
    port = 8080
    if len(sys.argv) >= 3:
        sconf[0] = sys.argv[1]
        port = sys.argv[2]
    # create the server
    s = Server(int(port), sconf)
    s.start()
