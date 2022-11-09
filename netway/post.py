from netway.parse import *
import socket 
import threading
from urllib.request import Request, urlopen
import urllib.request
import json 

class post:
    domain = None
    url = None
    http = None
    ip = None 
    tld = None 

    text = ''    
    status_code = 0
    headers = ''

    def __init__(agent,url,payload=None,headers=None,proxies=None):            
        post.url = getfull(url)
        post.domain = threading.Thread(target=getdomain,args=(url,)).start()
        post.http = threading.Thread(target=gethttp,args=(url,)).start()
        post.ip = threading.Thread(target=getip,args=(url,)).start()
        post.tld = threading.Thread(target=gettld,args=(url,)).start()

        if(payload!=None):
            if(header!=None and proxies!=None):
                prxy = proxies 
                hdata = headers
                resp = urlopen(Request(post.url,json.dumps(payload).encode('utf-8'),headers=hdata,proxies=prxy))
            elif(headers!=None and proxies==None):
                hdata = headers
                resp = urlopen(Request(post.url,json.dumps(payload).encode('utf-8'),headers=hdata))
            elif(headers==None and proxies==None):
                resp = urlopen(Request(post.url,json.dumps(payload).encode('utf-8')))

        elif(headers!=None):
            if(proxies==None and payload==None):
                hdata = headers
                resp = urlopen(Request(post.url,headers=hdata))

        elif(proxies!=None):
            if(payload==None and headers==None):
                prxy = urllib.request.FancyURLopener(proxies)
                resp = prxy.open(post.url)
                #print("A")


        elif(headers==None and payload==None and proxies==None):
            resp = urlopen(post.url)

        try:
            post.text = resp.read().decode('utf-8')
            post.status_code = resp.getcode()
            post.headers = resp.info()
        except:
            pass