class Vehicle:
    """Base class for all vehicle"""

    def __init__(self, name, color, brand):

        self.name = name
        self.color = color
        self.brand = brand

    def turn(self, direction):
        print("Turning", self.name, "to", direction)


class Car(Vehicle):
    """Car class"""

    def __init__(self, name, color, brand, year):
        super().__init__(name, color, brand)
        self.name = name
        self.color = color
        self.brand = brand
        self.year = year
        self.wheels = 4

    def change_gear(self, gear_name):
        """Method for gear change"""
        print(self.name, "is changing to", gear_name)

    def turn(self, direction):
        print(self.name, "is turning", direction)


if __name__ == "__main__":
    c = Car("Nusrat 5 GT force", "White", "RA", 2017)
    v = Vehicle("Rafi", "Black", "Afnan")

    c.change_gear("P")
    c.turn("Left")

    v.turn("Right")



