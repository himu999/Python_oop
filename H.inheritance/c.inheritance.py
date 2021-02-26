class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.color = color
        self.manufacturer = manufacturer

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):
        print("Turning", self.name, direction)

    def brake(self):
        print(self.name, "is stopping!")


class Car(Vehicle):
    """Car class"""

    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.wheels = 4
        print("A new car has been created. Name:", self.name)
        print("It has", self.wheels, "wheels")
        print("The car was bulit in", self.year)

        def change_gear(self, gear_name):
            """Method of changing gear"""
            print(self.name, "is changing gear to", gear_name)


if __name__ == "__main__":
    c = Car("Afnan GT 5.0 ", "N&R CC", "RED", 2015)







