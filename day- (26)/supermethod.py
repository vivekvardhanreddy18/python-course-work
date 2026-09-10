class whatsappv1:
    def status(x):
        print("You can uoload status for 24hrs")

class whatsappv2(whatsappv1):
    def status(x):
        super().status()
        print("You can add music and react")

a = whatsappv1
a.status()
b= whatsappv2
b.status()