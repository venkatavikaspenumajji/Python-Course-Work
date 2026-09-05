from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def withdraw(self):
        pass


class SBI(Bank):

    def withdraw(self):
        print("SBI withdrawal")

def senderinfo(self):
    print("you can enter their moblie number or scanner")

obj = SBI()
obj.withdraw()