class hotstar:

    def auth(x):
        print("yes you can login")

    def dashboard(x):
        print("You can see it")

    def search(x):
        print("You can search")

    def history(x):
        print("You can see history")

    def playcontrol(x):
        print("play, pause, resume")

    def ads(x):
        print("ads will run")

    def quality(x):
        print("You have limitrd quality")

    def devices(x):
        print("limited login")



class premiumhotstar(hotstar):
    def ads(x):
        print("ads wont run")

    def quality(x):
        print("high quality")

    def devices(x):
        print("Multiple logins")



vivek = hotstar()
v=dir(hotstar)
for i in v:
    if i.startswith("__"):
        continue
    k = getattr(hotstar, i)
if callable(k):
    k()