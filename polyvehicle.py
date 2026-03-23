class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("Driving on the road")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")


# Creating objects
car = Car()
bicycle = Bicycle()

# Demonstrating polymorphism
car.move()
bicycle.move()
