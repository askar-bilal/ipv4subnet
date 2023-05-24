import socket, struct

def ip2long(ip):
    return struct.unpack("!L", socket.inet_aton(ip))[0]

def long2ip(longip):
    return socket.inet_ntoa(struct.pack('!L', longip))


print(ip2long("192.168.1.2"))
print(long2ip(ip2long("192.168.1.2")))