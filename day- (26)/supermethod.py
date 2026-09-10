class whatsappv1:
    def status(x):
        print("You can uoload status for 24hrs")

class whatsappv2(whatsappv1):
    def status(x):
        super().status()
        print("You can add music and react")

a = whatsappv1()
a.status()
b= whatsappv2()
b.status()

# This method is super method , used

class whatsappv3:
    def status(x):
        print("you can call")



class whatsappv4(whatsappv1,whatsappv3):
    def status(x):
        whatsappv1.status(x)
        whatsappv3.status(x)
        print("You can create groups")