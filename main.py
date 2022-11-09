import netway

# Payload
proxy = {
  "socks5" : "socks5://51.38.191.151:80"
}
url = "https://api.ipify.org/"
nw = netway.get(url)
print(nw.text)
