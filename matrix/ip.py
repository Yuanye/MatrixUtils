# -*- coding: utf-8 -*- 
import socket, struct

def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

def long2ip(l):
    """
    Convert an long object to IP 
    """
    return socket.inet_ntoa(struct.pack('!L', l))

if __name__ == "__main__":
    pass

