import binascii
import socket
import struct
import sys

for string_address in ['192.168.1.1', '127.0.0.1']:
    packed = socket.inet_aton(string_address)
    print('Original:', string_address)
    print('Packed  :', binascii.hexlify(packed))
    print('Unpacked:', socket.inet_ntoa(packed))
    print()

"""
[root@huzhi-code 01_base]# python 11_socket_address_packing.py
('Original:', '192.168.1.1')
('Packed  :', 'c0a80101')
('Unpacked:', '192.168.1.1')
()
('Original:', '127.0.0.1')
('Packed  :', '7f000001')
('Unpacked:', '127.0.0.1')
()
[root@huzhi-code 01_base]#
"""