"""
   created at feb 06/20 by tir.farzad@gmail.com
   start up here

"""


class StartUp:
    def __init__(self):
        pass

    def __start_sockettcp_services__(self):
        """this function run sockettcp service
           :return:
        """
        from modules.services.sockettcp.socket_server import SocketServer

        SocketServer().run()

    def start(self):
        self.__start_sockettcp_services__()
