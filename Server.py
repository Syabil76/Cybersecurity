#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET specifies IPV4, SOCK_STREAM specifies connection (TCP/IP)

host = socket.gethostbyname()
#specifies host name and address etc.
#OR 
#host = 192.168.0.147 or otherwise

port = 444

serversocket.bind(host, port)
#binds the host TO the port 

serversocket.listen(3)
#specifies how many requests allowed

while True:
    clientsocket, address = serversocket.accept()
    #accepts connection
    print(f"recieved connection from {str(address)}")

    message = 'Welcome to server, sockets are fun' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
