#2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.
class Bankacc:
    def __init__(self,amount):
        self.amount=amount
    def deposit(self,deposit):
        self.amount+=deposit
        print(f"${deposit} is credited")
    def withdraw(self,withdraw):
        if withdraw<=self.amount:
            print(f"${withdraw} is withdrawn")
            self.amount-=withdraw
        else:
            print("Insufficient balance")
    def balance(self):
        print(f"Current balance is {self.amount}")
obj=Bankacc(0)
while True:
    n=int(input("Enter options :\n1)deposit\n2)withdraw\n3)checkbalance\n4)exit\n"))
    if n==1:
        deposit=int(input("Enter deposit amomunt : "))
        obj.deposit(deposit)
    elif n==2:
        withdraw=int(input("Enter withdraw amomunt : "))
        obj.withdraw(withdraw)
    elif n==3:
        obj.balance()
    else:
        break