import netway

data = {
  "content" : "Netway Post Methods!"
}


url = "https://discord.com/api/webhooks/1039783739099709470/p-4OTStZeKRd-fzXUQwXmUqMQAhPYIAiDCYj3NYQgpPL7a9SDB8t1nChkYnwiWsmgKxO"
nw = netway.post(url,data)

print(nw.text)