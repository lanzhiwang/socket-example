import socket


def get_constants(prefix):
    """Create a dictionary mapping socket module
    constants to their names.
    """
    return { getattr(socket, n): n for n in dir(socket) if n.startswith(prefix) }


protocols = get_constants('IPPROTO_')
print(protocols)
"""
{
0: 'IPPROTO_IP', 
1: 'IPPROTO_ICMP', 
2: 'IPPROTO_IGMP', 
4: 'IPPROTO_IPIP', 
6: 'IPPROTO_TCP', 
8: 'IPPROTO_EGP', 
12: 'IPPROTO_PUP', 
17: 'IPPROTO_UDP', 
22: 'IPPROTO_IDP', 
29: 'IPPROTO_TP', 
41: 'IPPROTO_IPV6', 
43: 'IPPROTO_ROUTING', 
44: 'IPPROTO_FRAGMENT', 
46: 'IPPROTO_RSVP', 
47: 'IPPROTO_GRE', 
50: 'IPPROTO_ESP', 
51: 'IPPROTO_AH', 
58: 'IPPROTO_ICMPV6', 
59: 'IPPROTO_NONE', 
60: 'IPPROTO_DSTOPTS', 
103: 'IPPROTO_PIM', 
255: 'IPPROTO_RAW'
}
"""

for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print('{:>4} -> {:2d} (socket.{:<12} = {:2d})'.format(
        name, proto_num, const_name,
        getattr(socket, const_name)))

"""
[root@huzhi-code 01_base]# python 08_socket_getprotobyname.py
icmp ->  1 (socket.IPPROTO_ICMP =  1)
 udp -> 17 (socket.IPPROTO_UDP  = 17)
 tcp ->  6 (socket.IPPROTO_TCP  =  6)
[root@huzhi-code 01_base]#
"""