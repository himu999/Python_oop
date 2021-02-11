import requests

img_url = "https://images.pexels.com/photos/1363876/pexels-photo-1363876.jpeg?cs=srgb&dl=pexels-travis-blessing-1363876.jpg&fm=jpg"

response = requests.get(img_url)

fp = open("h_background.png", "wb")

fp.write(response.content)