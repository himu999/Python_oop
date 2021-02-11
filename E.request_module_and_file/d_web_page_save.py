import requests

url = "https://www.premierfantasytools.com"

response = requests.get(url)

f = open("fantasy.html", "w", encoding=response.encoding)
f.write(response.text)

