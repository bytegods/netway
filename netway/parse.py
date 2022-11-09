import functools
from urllib.request import urlopen
import socket 

@functools.cache
def getip(url):
    return socket.gethostbyname(getdomain(url))


@functools.cache
def getdomain(url):
    if(url[len(url)-1]=='/'):
        url = url[:-1]
    else:
        pass

    if(url.startswith('http://')):
        url = url.split('http://')[1]
    elif(url.startswith('https://')):
        url = url.split('https://')[1]

    return url.split('/')[0]

@functools.cache
def getfull(url):
    return gethttp(url) + getdomain(url)

@functools.cache
def gethttp(domain):
    try:
        urlopen('https://'+domain).read()
    except:
        return 'http://'

    return 'https://'

@functools.cache
def gettld(url):
    return getdomain(url).split('.')[1]