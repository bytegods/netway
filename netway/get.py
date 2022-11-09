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

	@functools.cache
	def __init__(self,url):
		get.domain = getdomain(url)
		get.url = getfull(url)
		get.http = gethttp(url)
		get.ip = getip(url)
		get.tld = gettld(url)
		nw = urlopen(get.url)
		get.text = nw.read().decode("'latin-1'")
		get.headers = nw.info()
		get.status_code = nw.getcode()



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