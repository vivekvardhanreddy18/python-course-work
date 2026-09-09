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


class whatsappv3(whatsappv2):
    def groups(x):
        print('You can create groups and chat with multiple friends')


veeru = whatsappv3()
veeru.messege()
veeru.status()
veeru.groups()



