class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c

    def start(self):
        print("Starting the engine")


my_car = Car("Corolla", "white")
print(my_car.name)
print(my_car.color)

my_car.start()
