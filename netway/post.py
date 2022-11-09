from netway.parse import *
import socket 
import threading
from urllib import request, parse
#from urllib.request import urlopen
class post:
	domain = None
	url = None
	http = None
	ip = None 
	tld = None 

	text = ''
	status_code = 0
	headers = ''
	def __init__(agent,url,payload=None, **kwargs):
		# try:
		post.url = getfull(url)
		post.domain = threading.Thread(target=getdomain,args=(url,)).start()
		post.http = threading.Thread(target=gethttp,args=(url,)).start()
		post.ip = threading.Thread(target=getip,args=(url,)).start()
		post.tld = threading.Thread(target=gettld,args=(url,)).start()

		req =  request.Request(post.url, data=payload)
		resp = request.urlopen(req)

		post.text = resp.read().decode('utf-8')
		post.status_code = resp.getcode()
		post.headers = resp.info()
		# except Exception as e:
		# 	print(e)