class Car:

    def __init__(self, n, m, c, y, cc):
        self.name = n
        self.manufacturer = m
        self.color = c
        self.year = y
        self.cc = cc




    def start(self):
        print("Starting the engine")



    def break_system(self):
        print("Okay")


    def drive(self):
        print("Let's ")

    def turn(self):
        print("Left trun")

    def change_gear(self):
        print("Flexible")


car = Car("Tesla", "Digital Car", "Green", "2021", "210")

print("Car name is : ", car.name)
print("Manufacturer name is : ", car.manufacturer)
print("Color : ", car.color)
print("Exported year : ", car.year)
print("Engine capacity : ", car.cc + " cc", end="\n\n")

car.start()
car.break_system()
car.drive()
car.turn()
car.change_gear()