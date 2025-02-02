# Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse.
class Electronics:
    def move(self):
        print("Electronics method")
class MobileDevice(Electronics):
    def move(self):
        super().move()
        print("Mobile devices method")
class Smartphone(MobileDevice):
    def move(self):
        super().move()
        print("Smartphone method")
obj=Smartphone()
obj.move()