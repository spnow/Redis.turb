#!/usr/bin/python
import socket


class RedisTurb():
    def connect(self, host='localhost', port=6379):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def write(self, buffer):
        self.socket.sendall(buffer + '\r\n\r\n')
        return self.socket.recv(4096)

    def close(self):
        self.socket.close()

    """
    def scan(self, ip='127.0.0.1', port=6379):
        self.ip = ip.split('.')
        self.range = dict()
        alpha = ('a', 'b', 'c', 'd')
        for i, j in enumerate(alpha):
            self.range[j] = tuple(xrange(256)) if '*' in self.ip[i] else self.ip[i]
    """

    def auth(self, data):
        return self.write('AUTH ' + data)

    def info(self):
        return self.write('INFO')

    def config(self):
        return self.write('CONFIG GET *')

    def config_set(self, k, v):
        return self.write('CONFIG SET ' + k + v)

    def config_get(self, k, v):
        return self.write('CONFIG GET ' + k + v)

    def keys(self):
        return self.write('KEYS *')

    def fuzz(self, data):
        return self.write(data)

if __name__=="__main__":
    redis = RedisTurb()
