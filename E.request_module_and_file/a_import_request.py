import requests

response = requests.get("http://subeen.com//allposts")

print(response.ok)
print(response.reason)
print(response.status_code)
print()
res = requests.get("http://subeen.com//alllposts")
print(res.ok)
print(res.status_code)
print(res.reason)
