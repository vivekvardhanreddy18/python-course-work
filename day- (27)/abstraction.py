from abc import ABC,abstractmethod


class payment(ABC):
    def source(x):
        print("Scanner")
    def amount(x):
        print("Enter the amount")
    def bank(x):
        print("Select the bank")
    def pin(x):
        print("Enter the pin")
    @abstractmethod
    def paymentprocess(x):
        pass
    def paymentstatus(x):
        print("payment successfull")

class HDFC(payment):
    def paymentprocess(x):
        print("payment is processed through HDFC")
class ICICI(payment):
    def paymentprocess(x):
        print("payment is processed through ICICI")
class UNION(payment): 
    def paymentprocess(x):
        print("payment is processed through UNION")
class AXIS(payment):   
    def paymentprocess(x):
        print("payment is processed through AXIS")


vivek=HDFC()
vivek.source()
vivek.amount()
vivek.bank()
vivek.pin()
vivek.paymentprocess()
vivek.paymentstatus()
print()

vin=AXIS()
vin.source()
vin.amount()
vin.bank()
vin.pin()
vin.paymentprocess()
vin.paymentstatus()

    

    







