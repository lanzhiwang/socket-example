# -*- coding: utf-8 -*-

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()

"""
[root@huzhi-code 02_TCP_IP_Client_and_Server]# python 01_socket_echo_server.py
starting up on localhost port 10000
waiting for a connection
('connection from', ('127.0.0.1', 49448))
received 'This is the mess'
sending data back to the client
received 'age.  It will be'
sending data back to the client
received ' repeated.'
sending data back to the client
received ''
('no data from', ('127.0.0.1', 49448))
waiting for a connection
"""