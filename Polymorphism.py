# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling ")

# Testing polymorphism
vehicles = [Car(), Plane(), Bicycle()]

for v in vehicles:
    v.move()
