import datetime
import sys

from termcolor import colored


class lumberjack():
    def __init__(self, log_file):
        try:
            self.log_file = open(log_file, "a")
        except FileNotFoundError:
            print(colored("[-] ERROR: File not found: " + log_file, "red"))
            sys.exit(1)
        except PermissionError:
            print(colored("[-] ERROR: Can't open file: " + log_file, "red"))
            sys.exit(1)


    def print_message(self, prefix, message, color):
        full_message = "[{}] [{}] {}".format(
            prefix,
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            message
        )

        print(colored(full_message, color))

        self.log_file.write(full_message.strip() + "\n")


    def log_error(self, message):
        self.print_message("-", message, "red")


    def log_warning(self, message):
        self.print_message("!", message, "yellow")


    def log_info(self, message):
        self.print_message("+", message, "green")


    def log_debug(self, message):
        self.print_message("D", message, "cyan")

