# 4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        return f'Name:{self.name}, Roll.No:{self.roll}'

stu=Student("dgbfvs trdfbv",8520)
d=stu.display()
print(d)