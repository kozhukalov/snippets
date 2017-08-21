import socket
import threading
import sys
import select
import time

class LogServer(threading.Thread):
    def __init__(self, address="localhost", port=5514):
        self.port = port
        super(LogServer, self).__init__()
        self.socket = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM
        )
        while True:
            try:
                self.socket.bind((str(address), self.port))
            except socket.error:
                self.port += 1
                if self.port > port + 1000:
                    raise
                continue
            else:
                break
        self.rlist = [self.socket]
        self._stop = threading.Event()
        self._handler = self.default_handler

    def bound_port(self):
        return self.port

    @classmethod
    def default_handler(cls, message):
        pass

    def set_handler(self, handler):
        self._handler = handler

    def stop(self):
        self.socket.close()
        self._stop.set()

    def rude_join(self, timeout=None):
        self._stop.set()
        super(LogServer, self).join(timeout)

    def join(self, timeout=None):
        self.rude_join(timeout)

    def run(self):
        while not self._stop.is_set():
            r, w, e = select.select(self.rlist, [], [], 1)
            if self.socket in r:
                message, addr = self.socket.recvfrom(2048)
                self._handler(message)


server = LogServer()
server.start()
print server.bound_port()


try:
    print "Waiting for ^C"
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print "Stopping server"
    server.stop()
