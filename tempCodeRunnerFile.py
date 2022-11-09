
data = {
  "content": "Testing post method..."
}

url = "https://discord.com/api/webhooks/1039783739099709470/p-4OTStZeKRd-fzXUQwXmUqMQAhPYIAiDCYj3NYQgpPL7a9SDB8t1nChkYnwiWsmgKxO"
nw = netway.post(url,payload=data)
print(nw.text)