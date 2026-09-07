class flipkart:
    discount = 30  # 10% discount

    @classmethod
    def updateddiscount(cls):
        cls.discount = 40
        print("Updated discount:", cls.discount)

    def info(self,name, phno,address):
        self.name = name
        self.phno = phno
        self.address = address
        print("Welcome to Flipkart!",self.name)


    @staticmethod
    def offers():
        print("Current offers: Buy 1 Get 1 Free, Flat", flipkart.discount, "% off on Electronics")


vivek = flipkart()
vinith = flipkart()
vivek.info("vivek", 1234567890, "123 Main St")
vinith.info("vinith", 9987654321, "456 Oak Ave")
vivek.offers()

vinith.offers()

