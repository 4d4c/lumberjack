import sys

from termcolor import colored


class lumberjack():
    def __init__(self, log_file):
        try:
            self.log_file = open(log_file, "w+")
        except FileNotFoundError:
            print(colored("[-] ERROR: File not found: " + log_file, "red"))
            sys.exit(1)
        except PermissionError:
            print(colored("[-] ERROR: Can't open file: " + log_file, "red"))
            sys.exit(1)


    def log_error(self, message):
        pass


    def log_warning(self, message):
        pass


    def log_info(self, message):
        pass


    def log_debug(self, message):
        pass


Lumberjack("/tmp/test")
