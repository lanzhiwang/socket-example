import binascii
import socket
import struct
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.connect(server_address)

values = (1, b'ab', 2.7)
packer = struct.Struct('I 2s f')
packed_data = packer.pack(*values)

print('values =', values)

try:
    # Send data
    print('sending {!r}'.format(binascii.hexlify(packed_data)))
    sock.sendall(packed_data)
finally:
    print('closing socket')
    sock.close()

"""
[root@huzhi-code 06_Sending_Binary_Data]# python 01_socket_binary_client.py
('values =', (1, 'ab', 2.7))
sending '0100000061620000cdcc2c40'
closing socket
[root@huzhi-code 06_Sending_Binary_Data]#
"""