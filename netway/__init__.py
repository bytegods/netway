from netway.get import *
from netway.parse import * 
from netway.post import *
from netway.fast import *
from netway.scan import *

class debug:
    @functools.lru_cache(maxsize=16)
    def url(url):
        print(f"""
            Netway Debug...
            
    Domain Adress   : {getdomain(url)}
    HTTP or HTTPS   : {gethttp(url)}
    Full URL        : {getfull(url)}
    IP Adress       : {getip(url)}
    TLD Adress      : {gettld(url)}
    """)

