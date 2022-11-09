from netway.parse import *
from urllib import request, parse
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
	
	@functools.cache
	def __init__(agent,url,payload):
		print(payload)
		# try:
		post.domain = getdomain(url)
		post.url = getfull(url)
		post.http = gethttp(url)
		post.ip = getip(url)
		post.tld = gettld(url)
		
		payload = parse.urlencode(payload).encode()
		req =  request.Request(url, data=payload)
		rget = request.urlopen(req)
		print(rget.read())

		post.text = rget.read().decode('latin-1')
		post.status_code = rget.getcode()
		post.headers = rget.info()

		# except Exception as e:
		# 	print(e)
		# 	pass