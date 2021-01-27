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
        

def update_server_connections(server_addr, active_connections=0):
    """
    Prints in the screen some information about the server.

    It also formats it.
    """
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
