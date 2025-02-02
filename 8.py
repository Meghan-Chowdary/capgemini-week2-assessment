# 8. Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.

class Animal:
    def speak(self):
        print("Ranvijay is animal")
class Dog(Animal):
    def speak(self):
        print("bow bow")
class Cat(Animal):
    def speak(self):
        print("Meow meow")
obj1=Cat()
obj1.speak()
obj2=Dog()
obj2.speak()
obj3=Animal()
obj3.speak()