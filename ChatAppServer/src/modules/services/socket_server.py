"""
   created at feb 06/20 by tir.farzad@gmail.com
   this package handle socket server tcp

"""
from socket import (
    socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
 )
from utils.config_manager import ConfigManager
from .client_handler import ClientHandler


class SocketServer:
    """ this class create a socket stream on tcp protocol
    """
    def __init__(self):

        self.config_manager = ConfigManager()
        self.sock_connection = socket(AF_INET, SOCK_STREAM)
        self.sock_connection.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def __start__(self):
        """this function try to create a socket connection
           :return:
        """
        self.sock_connection.bind((
            self.config_manager.get.socket_server.IP,
            self.config_manager.get.socket_server.PORT
        ))
        self.sock_connection.listen(
            self.config_manager.get.socket_server.LISTEN_CLIENT
        )

    def run(self):
        """start server to listen clients
           :return: 
        """""
        client, client_address = self.sock_connection.accept()

        ClientHandler(
            client=client, client_address=client_address
        ).start()    #create cleint thread per cleint connected to server


