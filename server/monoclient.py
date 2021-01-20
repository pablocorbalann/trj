# This file contains the information for creating a socket for EACH 
# of the clients, it also contains the CLient class itself that is managed from the 
# server file (see server.py)
class ClientConfiguration:
    """
    Stores all the configuration for a simple client, for example the port
    or the ip address.
    """
    def __init__(self, conn, addr):
        """
        The constructor method for the ClientConfiguration class.

        Parameters
        ----------
        conn: 
            The connexion of the client
        addr: tuple
            A tuple (address) (<ip>, <port>)
        """
        self.conn = conn
        self.addr = addr 

    def __repr__(self):
        """
        Returns a simple representation of the configuration.

        Returns
        -------
        msg: str
            [<addr>]
        """
        return f"[{self.addr}]"

class Client:
    """
    Handles an specific client for the server.
    """
    def __init__(self, client_id, conf):
        """
        The constructor method for the Client class.

        Parameters
        ----------
        client_id: int
            A numeric value for make each of the client.
        conf: ClientConfiguration
            The instance that stores the configuration of the specific client.
        """
        self.client_id = client_id
        self.conf = conf
    
    def send(self, msg, dcf):
        """
        Sends an specific message to the client itself using a general server

        Parameters
        ----------
        msg: str
            The message itself
        dcf: str
            The decode format for sending the message
        """
        try:
            self.conf.conn.send(msg.encode(dcf))
        except Exception as e:
            print(f"{self.conf.__repr__()} E: {e}") 

    def recv(self, bites, dcf):
        """
        Receives a message from the server to then return it.

        Parameters
        ----------
        bites: int
            The maximum nº of bytes that the client can receive
        dcf: str
            The decode format of the bites.

        Returns
        -------
        msg: str
            The message
        """
        try:
            msg = self.conf.conn.recv(bites).decode(dcf)
            return msg
        except Exception as e:
            print(f"{self.conf.__repr__()}: {e}")
