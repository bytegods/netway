from urllib.request import urlopen
import socket
import json 

import threading

class get:
	# Advanced
	text = None 
	headers = None 
	status_code = None

	@functools.cache
	def __init__(self,url,**kwargs):

		nw = urlopen(url)
		try:
				get.text = nw.read().decode("utf-8")
		except:
    			get.text = nw.read().decode("latin-1")
		get.headers = nw.info()
		get.status_code = nw.getcode()
