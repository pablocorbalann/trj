# Thid file contains all the functions and classes that are used to decorate and
# make the server more beautifull.
#
# more information at: github.com/pblcc/trj
import os
import platform
import shutil
import sys

class Colors:
    """
    Contains the Asccii colors used in this script
    """
    INFO = "\033[96m"
    ERR = "\033[93m"
    OK = "\033[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"

def clear_screen():
    os.system("clear" if platform.system().lower() in ["linux", "java"] else "cls")

def exit(code=0):
    """Exits the complete app"""
    sys.exit(code)

def setup_yaml(yaml):
    """
    This function setups a server using a yaml file.

    Returns
    -------
    ip, port, dcf, bites
    """
    f = yaml["server"]
    return (
        f["ip"],
        f["port"],
        f["decode-format"],
        f["max-bites"],
        f["disconnect-message"],
        f["back-to-menu-message"]
    )

def print_server_options(options):
    """
    This function is used to print the server options using a format. It uses
    a parameter :param options: that has the form of:

        {
            1: message1,
            2: message2,
            ...
            n: messagen
        }

    And prints it like:
        [1] message1
        [2] message2
        [n] message3
    """
    colors = Colors()
    for i, option in options.items():
        print(f"{colors.INFO}[{i}]{colors.ENDC} {option}")

def print_decorated(ts, text):
    """
    Prints the text in a decorated way.

        | <text> <pad> |
    
    Parameters
    ----------
    ts -> The terminal size
    text -> The text to print
    """
    c = Colors()
    if ts.columns <= len(text):
        print(text)
    else:
        lt = len(text)
        separator = f"{c.INFO}|{c.ENDC}"
        spaces = " " * (ts.columns - lt - 2)
        print(f"{separator}{text}{spaces}{separator}")
        

def get_hash():
    """
    Returns the hash map of options the server can take.

    EG
        
        {
            1: name 1,
            2: name 2,
            ...
            n: name n
        }
    """
    return {
        0: "Close the server",
        1: "Broadcast a message"
    }

def update_server_connections(server_addr, active_connections=0):
    """
    Prints in the screen some information about the server.

    It also formats it.
    """
    print("here")
    # clear the screen
    clear_screen()
    c = Colors()
    ts = shutil.get_terminal_size() # columns and lines (c, l)
    # print the addr of the server
    server_addr = f"SERVER AT {server_addr[0]}-PORT {server_addr[1]}"
    print(f"{c.INFO}{server_addr}{c.ENDC}", end="")
    # print the active connections
    active_connections = f"ACTIVE CONNECTIONS: {active_connections}"
    lac = len(active_connections) + len(str(server_addr)) # lac stands for len of active connections (padXY)
    print(f"{' ' * (ts.columns - lac)}{c.INFO}{active_connections}{c.ENDC}")
    # print the options of the server
    print(print_server_options(get_hash()))
