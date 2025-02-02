# 9. Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `defAirplane`. Handle potential conflicts in the `move()` method

class Car:
    def move(self):
        print("car moves")
class Airplane:
    def move(self):
        print("Plane flies")
class Flyingcar(Airplane,Car):
    def move(self):
        super().move()
        print("flying car moves and flies")
obj=Flyingcar()
obj.move()