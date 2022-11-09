from netway.parse import *
from urllib.request import urlopen
import socket
import json 

import threading

class get:
	# Basic

	domain = None
	url = None
	http = None
	ip = None 
	tld = None 

	# Advanced

	text = None 
	headers = None 
	status_code = None
	#open_ports = []

	@functools.cache
	def __init__(self,url):
		get.url = getfull(url)
		get.domain = threading.Thread(target=getdomain,args=(url,)).start()
		get.http = threading.Thread(target=gethttp,args=(url,)).start()
		get.ip = threading.Thread(target=getip,args=(url,)).start()
		get.tld = threading.Thread(target=gettld,args=(url,)).start()

		nw = urlopen(get.url)
		try:
    			get.text = nw.read().decode("utf-8")
		except:
    			get.text = nw.read().decode("latin-1")
		get.headers = nw.info()
		get.status_code = nw.getcode()
		#get.open_ports = threading.Thread(target=getports,args=(url,)).start()



	# def json():
	# 	op = "{"
	# 	cl = "}"
	# 	return f'''{op}
	# 	"success": "{get.success}",

	# 	"domain":  "{get.domain}",
	# 	"url":     "{get.url}",
	# 	"I.P.":    "{get.http}",
	# 	"ip":      "{get.ip}",
	# 	"tld":     "{get.tld}",

	# 	"headers": "{get.headers}",
	# 	"status":  "{get.status_code}",
	# 	"text":    "{get.text}"

	# 	{cl}

	# 	'''