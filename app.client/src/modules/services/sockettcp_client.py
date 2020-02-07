"""
   created at feb 06/20 by tir.farzad@gmail.com
   this package act as client socket service to
   connecting server

"""
from socket import (
    socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
)


class SocketClientTCP:
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def __connect__(self):
        pass

