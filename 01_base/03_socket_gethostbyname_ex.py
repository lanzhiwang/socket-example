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
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print('  Hostname:', name)
        print('  Aliases :', aliases)
        print(' Addresses:', addresses)
    except socket.error as msg:
        print('ERROR:', msg)
    print()

"""
[root@huzhi-code 01_base]# python 03_socket_gethostbyname_ex.py
apu
('ERROR:', gaierror(-2, 'Name or service not known'))
()
pymotw.com
('  Hostname:', 'pymotw.com')
('  Aliases :', [])
(' Addresses:', ['66.33.211.242'])
()
www.python.org
('  Hostname:', 'dualstack.python.map.fastly.net')
('  Aliases :', ['www.python.org'])
(' Addresses:', ['151.101.228.223'])
()
nosuchname
('ERROR:', gaierror(-2, 'Name or service not known'))
()
[root@huzhi-code 01_base]#
"""