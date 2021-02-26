class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.color = color
        self.manufacturer = manufacturer

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

    def brake(self):
        print(self.name, "is stopping")


class Car(Vehicle):
    """Car class"""

    def change_gear(self, gear_name):
        """Method for changing gear"""

        print(self.name, "is changing gear to", gear_name)


if __name__ == "__main__":
    c = Car("Rafi_Elite 5.0 GT_force", "N&A Car and Co.", "Black")
    c.drive()
    c.turn("Left")
    c.change_gear("P")
