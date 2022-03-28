from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):  # class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already Open")  # As you see each read method gives different message
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already close")  # As you see each read method gives different
            # message
        self.opened = True

    @abstractmethod  # Means that any other class driven from this class should introduce its own class
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")


stream = MemoryStream()
"""
stream = Stream()  # Can't instantiate abstract class Stream with abstract method read
"""
netWork_read = NetworkStream()
