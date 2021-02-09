import requests

response = requests.get("https://www.rokomari.com/book")

print(response.ok)

print(response.text)

# print(type(response.text))
