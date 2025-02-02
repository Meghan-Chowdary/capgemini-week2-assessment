#12. Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently

class Payment:
    def process_payment(self,method):
        print(f"payment methos is {method}")
class CreditCardPayment(Payment):
    def process_payment(self):
        super().process_payment("credit card")
        print(f"we are using credit card")
class PayPalPayment(Payment):
    def process_payment(self):
        super().process_payment("pay pal")
        print(f"we are using paypal")
class BitcoinPayment(Payment):
    def process_payment(self):
        super().process_payment("Bitcoin")
        print(f"we are using Bitcoin")
ob1=BitcoinPayment()
ob1.process_payment()
ob2=PayPalPayment()
ob2.process_payment()
ob3=CreditCardPayment()
ob3.process_payment()