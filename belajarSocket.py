import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):


    def handle(self):
        self.data=self.request.recv(1024).strip()

        print(self.data)

        self.request.sendall("SELAMAT DATANG DI PORT 1234")


if__name__== "__main__":
    HOST, PORT = "localhost", 8088

    server = socketserver.TCPServer((HOST,PORT), MyTCPHandler)
    server.serve_forever()