from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount is: ",amount)

    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(car):
    def payment(self, amount):
        print('Your purchase amount of {} has exceeded your limit of $250 '.format(amount))

obj = DebitCardPayment()
obj.paySlip("$500")
obj.payment("$500")
    
