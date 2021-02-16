import requests
import sys

arg = sys.argv
base_url = "http://subeen.com/download/"
info_dt = {"name": "xx", "Email": "asia@gmail.com", "country": "Bangladesh"}

url = base_url + "process.php"

response = requests.post(url, info_dt)

# file_name = input("Enter the file name : ")
if response.ok is False:
    sys.exit("Error downloading the file")

# r = requests.get(url)


with open("book.pdf", "wb") as f:
    f.write(response.content)

print("Book download complete!")





