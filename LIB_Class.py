class InvalidOperationError(Exception):
    pass
# we use classes to bundle the data

class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already Open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already close")
        self.opened = True


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


stream = Stream()
netWork_read = NetworkStream()
stream.open()               # stream.opened is true
print(stream.opened)        # True
print(netWork_read.opened)  # False
netWork_read.open()         # netWork_read.opened is True
print(netWork_read.opened)  # True
file_Read = FileStream()
file_Read.read()
netWork_read.read()
