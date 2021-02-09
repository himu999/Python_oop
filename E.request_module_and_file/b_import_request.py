import requests

response = requests.get("http://example.com")

print(response.ok)

print(response.text)

# print(type(response.text))
