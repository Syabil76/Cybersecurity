#!/bin/python3

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#where AF_INET = the ipv4 address of the server and the SOCK_STREAM is the socket type

server.bind((socket.gethostname(), 1234))
server.listen(5)


