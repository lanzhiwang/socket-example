#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

HOSTS = [
    'apu',
    'pymotw.com',
    'www.python.org',
    'nosuchname',
]

for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host, msg))

"""
[root@huzhi-code 01_base]# python 02_socket_gethostbyname.py
apu : [Errno -2] Name or service not known
pymotw.com : 66.33.211.242
www.python.org : 151.101.228.223
nosuchname : [Errno -2] Name or service not known
[root@huzhi-code 01_base]#
"""