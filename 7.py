# 7. Create a multi-level class structure with `Person` → `Employee` → `Manager`, where `Manager` has an additional method `approve_leave()`.

class Manager:
    def manager(self):
        print("This is manager class")
    def approve(self):
        print("Leave approved")
class Employee(Manager):
    def employee(self):
        print("This is employee class")
        
class Person(Employee):
    def person(self):
        print("This is person class")

d=Person()
d.person()
d.employee()
d.manager()
d.approve()