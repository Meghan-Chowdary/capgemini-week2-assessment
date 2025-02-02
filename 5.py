# 5. Create a `Product` class with attributes `name`, `price`, and `stock`. Write a method `check_availability(quantity)` that returns whether the requested quantity is available.

class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,quantity):
        return self.stock>=quantity
qua=int(input("enter quantity"))
obj=Product("sgbvsrt",563,8)
if(obj.check_availability(qua)):
    print("quantity available")
else:
    print("quantity not available")