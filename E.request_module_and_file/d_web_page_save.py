import requests
import os
import webbrowser as wb

url = "https://www.premierfantasytools.com"

response = requests.get(url)

f = open("fantasy.html", "w", encoding=response.encoding)
f.write(response.text)

file_path = os.path.relpath("fantasy.html")
print(file_path)

wb.open("file://" + file_path)



