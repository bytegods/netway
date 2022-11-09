from netway.parse import *
import socket

@functools.cache
def ports(url):
    ip = socket.gethostbyname(getdomain(url))
    openp = []
    ports = [20,21,22,23,53,25,40,44,69,80,139,137,443,444,445,4444,8080, 8443]
    ports.sort()
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            check = s.connect_ex((ip,port))
            if(check==0):
                version = None
                openp.append(port)
        except:
            pass
    s.close()
    return openp