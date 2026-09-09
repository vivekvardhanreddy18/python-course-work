class Instagram:
    def __init__(self,username,pw):
        self.username = username
        self.__pw = pw
        print(f"Welcome to Instagram {self.username}")


vivek = Instagram('vivek' , '123465')
