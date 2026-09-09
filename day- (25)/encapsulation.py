class Instagram:
    def __init__(x,username,pw):
        x.username = username
        x.__pw = pw
        x._post = []

    def getpw(x):
        return x.__pw

    @property
    def accesspost(x):
        return x._post

vivek = Instagram('vivek', '123456')
print(vivek.username)
print(vivek.getpw())
print(vivek.accesspost)






