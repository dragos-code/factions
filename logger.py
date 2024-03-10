
import os
import sys
from datetime import datetime

class Logger(object):
    def __init__(self, directory="logs", filename="log"):
        self.check_and_create_log_directory(directory)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filepath = os.path.join(directory, f"{filename}_{timestamp}.log")
        self.terminal = sys.stdout
        self.log = open(filepath, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # This flush method is needed for python 3 compatibility.
        # It handles the flush command by doing nothing.
        # You might want to specify some extra behavior here.
        pass

    @staticmethod
    def check_and_create_log_directory(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
