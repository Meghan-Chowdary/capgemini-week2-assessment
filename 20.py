# Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes
from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        print("logged in Google")
    def logout(self):
        print("logged out of Google ")
class FacebookAuth(UserAuthentication):
    def login(self):
        print("logged in Facebook")
    def logout(self):
        print("logged out Facebook")
google=GoogleAuth()
google.login()
google.logout()
facebook=FacebookAuth()
facebook.login()
facebook.logout()