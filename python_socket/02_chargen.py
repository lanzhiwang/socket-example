#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys

def get_message():
    alphabet = "".join(chr(x) for x in range(33, 127))
    alphabet += alphabet
    return "\n".join(alphabet[x:x+72] for x in range(127-33)) + "\n"


def chargen(sock):
    message = get_message()
    # print len(message)
    try:
        while True:
            sock.sendall(message)
    except:
        pass


def main(argv):
    if len(argv) < 3:
        binary = argv[0]
        print "Usage:\n  %s -l port\n  %s host port" % (argv[0], argv[0])
        """
        Usage:
            02_chargen.py -l port
            02_chargen.py host port
        """
        return
    port = int(argv[2])
    print port  # 8888
    if argv[1] == "-l":
        # server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', port))
        server_socket.listen(5)
        listen_addr = server_socket.getsockname()
        print 'Listen on %s:%d' % listen_addr  # Listen on 0.0.0.0:8888
        while True:
            (client_socket, client_address) = server_socket.accept()
            chargen(client_socket)
    else:
        # client
        sock = socket.create_connection((argv[1], port))
        print 'Client connected ', sock.getsockname(), sock.getpeername()
        chargen(sock)


if __name__ == "__main__":
    # print sys.argv
    """
    $ python 02_chargen.py -l port
    ['02_chargen.py', '-l', 'port']
     
    $ python 02_chargen.py host port
    ['02_chargen.py', 'host', 'port']
    """
    main(sys.argv)



"""
作为服务端使用
[root@huzhi-code python_socket]# python 02_chargen.py -l 8888

[root@huzhi-code python_socket]# curl 127.0.0.1:8888
jklmnopqrstuvwxyz{|}~!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRS

"""