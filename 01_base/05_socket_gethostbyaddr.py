import socket

hostname, aliases, addresses = socket.gethostbyaddr('10.9.0.10')

print('Hostname :', hostname)
print('Aliases  :', aliases)
print('Addresses:', addresses)

"""
[root@huzhi-code 01_base]# python 05_socket_gethostbyaddr.py
Traceback (most recent call last):
  File "05_socket_gethostbyaddr.py", line 3, in <module>
    hostname, aliases, addresses = socket.gethostbyaddr('10.9.0.10')
socket.herror: [Errno 2] Host name lookup failure
[root@huzhi-code 01_base]#

"""
