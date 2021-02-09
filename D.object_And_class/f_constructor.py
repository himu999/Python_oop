class Car:

    def __init__(self, n, c, y):
        self.name = n
        self.color = c
        self.year = y

        """here __init__ is a constructor"""

    def start(self):
        print("Car name is : ", self.name)
        print("Car color is : ", self.color)
        print("Car color is : ", self.year, end="\n\n")


print("First object:")
my_car = Car("Tesla", "green", "1995")
my_car.start()


print("Second object:")
my_car1 = Car("Corolla", "yellow", "1995")
my_car1.start()
