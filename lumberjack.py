import datetime
import sys

from termcolor import colored


class Lumberjack():
    """
    Logging class that prints to console and file.

    log_filename : Output filename
    print_debug  : Print debug messages to console
    console_time : Print timestamps to console
    """

    def __init__(self, log_filename=False, print_debug=False, console_time=True):
        self.console_time = console_time
        self.print_debug = print_debug

        try:
            if log_filename:
                self.log_filename = log_filename
                with open(log_filename, "a") as log_file:
                    log_file.write("\n" + "#" * 80 + "\n\n")
            else:
                self.log_filename = False
        except FileNotFoundError:
            print(colored("[-] ERROR: File not found: " + log_filename, "red", attrs=['bold']))
            sys.exit(1)
        except PermissionError:
            print(colored("[-] ERROR: Can't open file: " + log_filename, "red", attrs=['bold']))
            sys.exit(1)


    def print_message(self, prefix, message, color):
        if self.console_time:
            full_message = "[{}] [{}] {}".format(
                prefix,
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                message
            )
        else:
            full_message = "[{}] {}".format(
                prefix,
                message
            )

        # Check if we need to print DEBUG message to console
        if not self.print_debug and prefix == "D":
            pass
        else:
            print(colored(full_message, color, attrs=['bold']))

        if self.log_filename:
            with open(self.log_filename, "a") as log_file:
                log_file.write(full_message.strip() + "\n")


    def error(self, message):
        self.print_message("-", message, "red")


    def warning(self, message):
        self.print_message("!", message, "yellow")


    def info(self, message):
        self.print_message("+", message, "green")


    def debug(self, message):
        self.print_message("D", message, "cyan")
