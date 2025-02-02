# Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`
class Notification:
    def send(self):
        print("this is notification")
class EmailNotification(Notification):
    def send(self):
        print("email notification")
class SMSNotification(Notification):
    def send(self):
        print("Sms notification")
notification=Notification()
email=EmailNotification()
sms=SMSNotification()
notification.send()
email.send()
sms.send()