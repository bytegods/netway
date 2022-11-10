# Netway ![](https://visitor-badge.glitch.me/badge?page_id=bytegods.netway)

<div> 
  <p align="center">
    <img src="https://github.com/bytegods/netway/blob/main/assets/png/logo.png?raw=true" width="400"> 
  </p>
</div>

Netway is internet library that allows you to use internet. Example use get and post methods on websites, create network server and client side scripts and more...


## Installation
```python
pip install netway
```

## Usage
Note : Dont forget to use https or http while using get and post methods...

* Simple **GET** Request :
```python
import netway 

nw = netway.get("https://google.com/")
print(nw.headers)

# Avaliable GET Modules : 
# .text 
# .headers
# .status_code
```

* Simple **POST** Request :
```python
import netway

# Payload

payload = {
  "requestType": "EMAIL_SIGNIN",
  "email": "jomavex666@hoxds.com",
  "continueUrl": "https://fireship.io/",
  "canHandleCodeInApp": True
}
proxy = {
  "http" : "51.38.191.151:80"
}
header = {
  "Content-Type" : "bla bla"
}
url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=AIzaSyBns4UUCKIfb_3xOesTSezA9GbEyuIU7XA"
nw = netway.post(url,payload=data,proxies=proxy,headers=header)
print(nw.text)
# headers=header
# proxies=proxy_dict
# payload=data

# you are free to use them... Examples : 
# nw = netway.post(url)
# nw = netway.post(url,payload=data)
#...

# Avaliable POST Modules : 

# proxies = proxy
# headers = header
# payload = data 
# .text 
# .headers
# .status_code
```
You can use same **GET** modules for **POST** request.