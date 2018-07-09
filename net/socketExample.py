import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):


    def handle(self):
        self.data=self.request.recv(1024).strip()
        print(self.data)


        balasan = bytes("udh sukses??","utf-32")
        self.request.sendall(balasan)


if __name__ == "__main__":
    HOST, PORT = "192.168.0.4", 8088
    server = socketserver.TCPServer((HOST,PORT), MyTCPHandler)
    server.serve_forever():