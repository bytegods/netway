# Netway ![](https://visitor-badge.glitch.me/badge?page_id=bytegods.netway)

<div> 
  <p align="center">
    <img src="assets/svg/logo.svg" width="400"> 
  </p>
</div>

Large Network library for python.


## Installation
```python
pip install netway
```

## Usage

* Simple **GET** Request :
```python
import netway 

nw = netway.get("https://google.com/")
print(nw.headers)

# Avaliable GET Modules : 

# .domain
# .url
# .http
# .ip 
# .tld

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

url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=AIzaSyBns4UUCKIfb_3xOesTSezA9GbEyuIU7XA"
nw = netway.post(url,payload=data)
print(nw.text)

# Avaliable GET Modules : 

# .domain
# .url
# .http
# .ip 
# .tld

# .text 
# .headers
# .status_code
```
You can use same **GET** modules for **POST** request.