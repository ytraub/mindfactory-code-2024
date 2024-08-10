import socket
import json

SIZE = 1024


class RPCClient:
    def __init__(self, host: str = "localhost", port: int = 8080) -> None:
        self.__sock = None
        self.__address = (host, port)

    def connect(self):
        try:
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__sock.connect(self.__address)
        except EOFError as e:
            print(e)
            raise Exception("Client was not able to connect.")

    def disconnect(self):
        try:
            self.__sock.close()
        except:
            pass

    def __getattr__(self, __name: str):
        def excecute(*args, **kwargs):
            self.__sock.sendall(json.dumps((__name, args, kwargs)).encode())

            response = json.loads(self.__sock.recv(SIZE).decode())

            return response

        return excecute
