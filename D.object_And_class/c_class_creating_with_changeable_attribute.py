class Car:
    name = ""
    color = ""
    price = "20 million $"

    def start():
        print("Starting the engine")


Car.name = "Tesla"
Car.color = "black"

print("Name of the car:", Car.name)
print("Color :", Car.color)
print("Price :", Car.price)

Car.start()
