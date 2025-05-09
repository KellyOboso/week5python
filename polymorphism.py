class Animal:
    def move(self):
        print("Animal moves in some way.")

class Dog(Animal):
    def move(self):
        print("Walking")

class Fish(Animal):
    def move(self):
        print("Swimming")

class Vehicle:
    def move(self):
        print("Vehicle moves in some way.")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

if __name__ == "__main__":
    # Create instances
    dog = Dog()
    fish = Fish()
    car = Car()
    plane = Plane()

    # Store in a list to demonstrate polymorphism
    movers = [dog, fish, car, plane]

    for mover in movers:
        mover.move()
