class Car:

    def __init__(self, n, c):
        self.name = n
        self.color = c

        """here __init__ is a constructor"""

    def start(self):
        print("Car name is : ", self.name)
        print("Car color is : ", self.color, end="\n\n")


print("First object:", end="\n")
my_car = Car("Tesla", "green")
my_car.start()


print("Second object:")
my_car1 = Car("Corolla", "yellow")
my_car1.start()
