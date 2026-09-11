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
        print("Payment successfull")

class HDFC(Payment):
    def paymentprocess(x):
        print("Payment is processed through HDFC")
class ICICI(Payment):
    def paymentprocess(x):
        print("Payment is processed through ICICI")
class UNION(Payment): 
    def paymentprocess(x):
        print("Payment is processed through UNION")
class AXIS(Payment):   
    def paymentprocess(x):
        print("Payment is processed through AXIS")


vivek=HDFC()
vivek.source()
vivek.amount()
vivek.bank()
vivek.pin()
vivek.paymentprocess()


    

    







