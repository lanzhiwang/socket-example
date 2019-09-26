import socket

for host in ['apu', 'pymotw.com', 'baidu.com']:
    print('{:>10} : {}'.format(host, socket.getfqdn(host)))

"""
[root@huzhi-code 01_base]# python 04_socket_getfqdn.py
       apu : apu
pymotw.com : pymotw.com
 baidu.com : baidu.com
[root@huzhi-code 01_base]#
"""