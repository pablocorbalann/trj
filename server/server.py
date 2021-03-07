import socket
import threading
import sys

import monoclient
import decorators
import loads


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
        print(f"{colors.ERR}Error, invalid value for base 10 {e}{colors.ENDC}")
    except Exception as e:
        print(f"{colors.ERR}Error, invalid iteral / option... {e}{colors.ENDC}")
    return option


class ServerConfiguration:
    """
    The class is used to handle all the configuration for an specific 
    server, and capsule it.
    """

    def __init__(self, port, ip, dcf, bites, dmsg, emsg):
        """
        The constructor method for the ServerConfiguration class.

        From here all the attributes of the class are created.
        
        Parameters
        ----------
        port: int
            The port of the server
        ip: str
            The ip address of the server
        dcf: str
            The format the server uses 
        bites: int
            The maximum number of bites of the 
            server.
        """
        self.__port = port
        self.__ip = ip
        self.__dcf = dcf
        self.__bites = bites
        self.__disconnect_msg = dmsg
        self.__exit_msg = emsg

    def __repr__(self):
        """
        Returns a short representation of all the information.
        """
        return f"{self.get_port()}: {self.get_ip()}"

    def setup_server(self):
        """
        Set ups the complete server using the return statement.

        Returns
        -------
            port, ip, dcf, bites
        """
        return (
            self.get_port(),
            self.get_ip(),
            self.get_dcf(),
            self.get_bites(),
            self.get_dmsg(),
            self.get_emsg()
        )

    def get_port(self):
        return self.__port

    def get_ip(self):
        return self.__ip

    def get_dcf(self):
        return self.__dcf

    def get_bites(self):
        return self.__bites

    def get_dmsg(self):
        return self.__disconnect_msg

    def get_emsg(self):
        return self.__exit_msg


class Server:
    """
    This class is used to manage all the servers trj uses and to manage
    the sockets.
    """

    def __init__(self, conf):
        """
        This is the constructor method for the Server class, from here all the
        attributes of the class are created

        Parameters
        ----------
        conf: ServerConfiguration
            The configuration of the sever
        """
        self.port, self.ip, self.dcf, self.bites, dmsg, emsg = conf.setup_server()

        self.addr = (self.ip, self.port)
        self.__loop_thread = None

        self.disconnect = dmsg  # msg to disconnect
        self.exit_command = emsg

        # create the actual server of the instance
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.settimeout(10.0)
        self.server.bind(self.addr)  # bind the server to the addr

        self.clients = {}  # stores configuration of each client

        # colors
        self.__colors = decorators.Colors()

        # loop hash for the options
        self.__loop_func_hash = {
            0: self.__close,
            1: self.__send_to_all_clients
        }

    def __close(self):
        """
        Closes all the clients and then closes the server and exits the app.
        """
        for client in self.clients:
            client.close()
        self.clients = []
        print("Press CTRL+C 2 times to exit the server...")
        decorators.exit()

    def __send_to_all_clients(self):
        """
        Request a command and sends that command to all the clients connected

        (kind of a broadcast)
        """
        print(f"Remember to type {self.exit_command} for going back to the menu...")
        while True:
            command = input(">>> ")
            if command == self.exit_command:
                break
            cdr = []  # client data register
            for i, client in self.clients.items():
                try:
                    client.send(command, self.dcf)
                    client_data = client.recv(self.bites, self.dcf)
                    cdr.append(client_data)
                except socket.timeout as e:
                    print(f"One client doesn't respond to the server: {client}")
            print(f"{self.__colors.INFO}{command} sended to {len(cdr)} clients{self.__colors.ENDC}")

    def __loop(self):
        """
        This method is used to loop the options and depending on what the
        server manager types, it will invoke other methods.
        """
        looping = True
        # create the simple hash
        while looping:
            key = 0
            # Print the options
            decorators.print_server_options(decorators.get_hash())
            key = request_server_option()
            # Get the option and start the hash map 
            try:
                if key == 0:
                    self.__close()
                    decorators.exit()
                else:
                    print(f"Eecuting function {key}...")
                    self.__loop_func_hash[key]()  # the position 0 is the function
            except KeyError as e:
                print(f"{self.__colors.ERR}Invalid option... {key}{self.__colors.ENDC}")
                self.__close()
            except Exception as e:
                print(f"{self.__colors.FAIL}Internal crash at looping options... {e}{self.__colors.ENDC}")
                self.__close()

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
        print(f"\n{self.__colors.INFO}[NEW CONNECTION] {client.conf.addr} connected.{self.__colors.ENDC}")
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
        running = True
        while running:
            try:
                self.server.settimeout(None)
                conn, addr = self.server.accept()
                client_configuration = monoclient.ClientConfiguration(conn, addr)
                # ct stands for client total (the counter of the client)
                ct = len(self.clients)
                # create the thread for the self.handle_client method
                thread = threading.Thread(target=self.__handle_client, args=[ct, client_configuration])
                thread.start()
                # check if the loop thread is already working, if it's restart it.
                if self.__loop_thread is not None:
                    # If the loop thread is not equal to none, we should end this 
                    # thread and reset it to None.o
                    self.__loop_thread.join()
                    self.__loop_thread = None
                # Set the loop thread to  the actual thread
                self.__loop_thread = threading.Thread(target=self.__loop)
                self.__loop_thread.start()
            except Exception as e:
                # report the bug informing the user
                print(f"[SERVER CRASH]: Fatal error, {e}")


def main(port, ip, dcf, bites, dmsg, emsg):
    """
    This function actually starts running the server, using 4
    parameters.
    """
    server_configuration = ServerConfiguration(port, ip, dcf, bites, dmsg, emsg)
    if "-c" in sys.argv:
        print(f"SERVER CONFIGURATION: {server_configuration.setup_server()}")
    server = Server(server_configuration)
    server.start()


if __name__ == '__main__':
    ip, port, dcf, bites, dmsg, emsg = decorators.setup_yaml(loads.load_configuration())
    # actually run the server
    # check if the user did python3 server.py <ip> <port>
    # create the server
    arg = sys.argv
    if len(arg) >= 3:
        ip = arg[1]
        port = int(arg[2])
    main(port, ip, dcf, bites, dmsg, emsg)
