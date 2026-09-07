class flipkart:
    discount = 0.1  # 10% discount

    def info(self,name, phno,address):
        self.name = name
        self.phno = phno
        self.address = address
        print("Welcome to Flipkart!",self.name)


vivek = flipkart()
vinith = flipkart()
vivek.info("vivek", 1234567890, "123 Main St")
vinith.info("vinith", 9987654321, "456 Oak Ave")
