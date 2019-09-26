import binascii
import socket
import struct
import sys

string_address = '2002:ac10:10a:1234:21e:52ff:fe74:40e'
packed = socket.inet_pton(socket.AF_INET6, string_address)

print('Original:', string_address)
print('Packed  :', binascii.hexlify(packed))
print('Unpacked:', socket.inet_ntop(socket.AF_INET6, packed))

"""
[root@huzhi-code 01_base]# python 12_socket_ipv6_address_packing.py
('Original:', '2002:ac10:10a:1234:21e:52ff:fe74:40e')
('Packed  :', '2002ac10010a1234021e52fffe74040e')
('Unpacked:', '2002:ac10:10a:1234:21e:52ff:fe74:40e')
[root@huzhi-code 01_base]#
"""