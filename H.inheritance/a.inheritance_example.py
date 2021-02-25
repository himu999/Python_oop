class Vehicle:

    """
    Base class for all vehicle
    """

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving", self.name, self.color)

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

    def brake(self):
        print(self.name, "is stopping!")


if __name__ == "__main__":
    v1 = Vehicle("Fusion 110 EX", "Walton", "Black")
    v2 = Vehicle("Softail Delux", "Harley-Davidson", "Blue")
    v3 = Vehicle("Mustang 5.0 GT Coupe", "Ford", "Red")

    v1.drive()
    v2.drive()
    v3.drive()

    print("\n")

    v1.turn("left")
    v2.turn("right")

    print()

    v1.brake()
    v2.brake()
    v3.brake()
