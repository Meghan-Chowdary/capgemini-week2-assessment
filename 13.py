# Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`
class Shape:
    def area(self,area):
        print(f"area formula is {area}")
class Square(Shape):
    def area(self):
        super().area("a*a")
        print("area is square of one side")
class Triangle(Shape):
    def area(self):
        super().area("0.5*b*h")
        print("area is half product of base and height")
sq=Square()
sq.area()
tri=Triangle()
tri.area()