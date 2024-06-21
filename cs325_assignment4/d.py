from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console Log: {message}")

class FileLogger(Logger):
    def log(self, message):
        with open('log.txt', 'a') as file:
            file.write(f"File Log: {message}\n")

class Application:
    def __init__(self, logger):
        self.logger = logger

    def do_something(self):
        self.logger.log("Doing something important")
