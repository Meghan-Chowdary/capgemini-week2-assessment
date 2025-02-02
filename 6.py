# 6. Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`

class Vehicle:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
    def display(self):
        print(f"name:{self.name} model:{self.model} year:{self.year}(parent class)")
class Car(Vehicle):
    def __init__(self,name,model,year,windows):
        super().__init__(name,model,year)
        super().display()
        self.windows=windows
    def display(self):
        print(f"this has {self.windows} windows")
class Bike(Vehicle):
    def __init__(self,name,model,year,Gears):
        super().__init__(name,model,year)
        super().display()
        self.Gears=Gears
    def display(self):
        print(f"this has {self.Gears} Gears")
class ElectricCar(Car):
    def __init__(self,name,model,year,windows,backup):
        super().__init__(name,model,year,windows)
        super().display()
        self.backup=backup
    def display(self):
        print(f"battery backup is {self.backup}")

car=Car("Maruthi","Swift",2021,5)
car.display()
bike=Bike("Hero Honda","splendor ismart",2016,4)
bike.display()
ev=ElectricCar("Tesla","prime",2050,5,"50 hours")
ev.display()