class Vehicle:
    def move(self):
        print("This vehicle is moving.")
class car(Vehicle):
    def move(self):
        print("Driving on the road")
class Bicycle(Vehicle):
    def move(self):
        print("pedaling on the road")
#demonstrating polymorphism
Vehicle = [car(), Bicycle()]

for Vehicle in Vehicle:
    Vehicle.move()