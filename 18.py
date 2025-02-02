# 18. Implement an abstract class `ICalculator` with methods ``, `subtract()`, `multiply()`, and `divide()`. Create a `BasicCalculator` class that implements these methods.
from abc import ABC,abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    @abstractmethod
    def sub(self,a,b):
        pass
    @abstractmethod
    def mul(self,a,b):
        pass
    @abstractmethod
    def div(self,a,b):
        pass
class BasicCalculator(ICalculator):
    def add(self,a,b):
        print(f"{a+b}")
    def sub(self,a,b):
        print(f"{a-b}")
    def mul(self,a,b):
        print(f"{a*b}")
    def div(self,a,b):
        print(f"{a/b}")

cal=BasicCalculator()
cal.add(5,5)
cal.sub(5,5)
cal.mul(5,5)
cal.div(5,5)