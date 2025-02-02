# 16. Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.
from abc import ABC,abstractmethod
class Ishape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rect(Ishape):
    def calculate_area(self,l,b):
        print(f"{l*b}")
class Circle(Ishape):
    def calculate_area(self,r):
        print(f"{22.7*r*r}")
rect=Rect()
rect.calculate_area(5,5)
cir=Circle()
cir.calculate_area(5)