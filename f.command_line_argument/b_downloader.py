import requests
import sys

arg = sys.argv

arg.append(input("Enter image url : "))
arg.append(input("Enter file name : "))

img_url = arg[1]
file_name = arg[2]

r = requests.get(img_url)

with open(file_name, "wb") as f:
    f.write(r.content)

