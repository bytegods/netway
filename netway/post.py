from netway.parse import *
from urllib.request import urlopen
import socket
import json 

class post:
	domain = None
	url = None
	http = None
	ip = None 
	tld = None 

	# Advanced

	text = None 
	headers = None 
	status_code = None
    def __init__(agent,url,payload):
	post.domain = getdomain(url)
	post.url = getfull(url)
	post.http = gethttp(url)
	post.ip = getip(url)
	post.tld = gettld(url)

        payload = parse.urlencode(payload).encode()
        req =  request.Request(post.url, data=payload)
        rget = request.urlopen(req)

        post.text = rget.read().decode()
        post.status_code = rget.getcode()
        post.headers = rget.info()
