class Car:
    name = "Premio"
    color = "white"

    @staticmethod
    def start():
        print("Starting the engine")


print("Name of the car :", Car.name)
print("Color : ", Car.color)
Car.start()
