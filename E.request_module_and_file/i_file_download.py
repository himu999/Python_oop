import requests

url = "https://images.pexels.com/photos/6749092/pexels-photo-6749092.jpeg?cs=srgb&dl=pexels-chris-tombrella-6749092.jpg&fm=jpg"

request = requests.get(url)

with open("i.png", "wb") as f:
    f.write(request.content)

