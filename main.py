import netway

data = {
  "requestType": "EMAIL_SIGNIN",
  "email": "jomavex666@hoxds.com",
  "continueUrl": "https://fireship.io/",
  "canHandleCodeInApp": True
}

url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=AIzaSyBns4UUCKIfb_3xOesTSezA9GbEyuIU7XA"
nw = netway.post(url,payload=data)
print(nw.text)