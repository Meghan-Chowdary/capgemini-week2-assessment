# Class and Object
# •	1. Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.

class Employee:
    def __init__(self,name,id,dep):
        self.name=name
        self.id=id
        self.dep=dep
    def details(self):
        print(f"name:{self.name}\nid:{self.id}\ndepartment:{self.dep}\n")
name=input("Enter name : ")
id=int(input("Enter id : "))
dep=input("Enter department : ")
obj=Employee(name,id,dep)
obj.details()