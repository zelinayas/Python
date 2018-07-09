import socket

HOST, PORT = "192.168.0.3", 8088

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    sock.connect((HOST,PORT))
    sock.sendall(bytes("Q","utf-8"))
    balasan = str(sock.recv(1024),"utf-8")

finally:
    sock.close()

print(balasan)