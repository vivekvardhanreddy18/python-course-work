class whatsappv1:
    def messege(x):
        print('You can send messege to your friends')


class whatsappv2(whatsappv1):
    def status(x):
        print('You can upload status to your friends')
vinith = whatsappv1()
vinith.messege()

vivek = whatsappv2()
vivek.messege() 
vivek.status()

# This is single inheritance where whatsappv2 class is inheriting the properties of whatsappv1 class.


class whatsappv3(whatsappv2):
    def groups(x):
        print('You can create groups and chat with multiple friends')


veeru = whatsappv3()
veeru.messege()
veeru.status()
veeru.groups()

# This is multi-level inheritance where whatsappv3 inheriting from whatsappv2 and whatsappv2 inheriting from whatsappv1 class.


class whatsappv4(whatsappv3,whatsappv1):
    def video_call(x):
        print('You can make video call to your friends')

rushi = whatsappv4()
rushi.messege() 
rushi.status()
rushi.groups()
rushi.video_call()

# This is multiple inheritance where whatsappv4 class is inheriting the properties of whatsappv3 and whatsappv1 class.

