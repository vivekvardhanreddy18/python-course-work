class redbus:
    bus={i: "Available" for i in range(1,11)}

    def displayseat(x):
        print("--------MVR Travels--------")
        from abc import ABC, abstractmethod


        class Payment(ABC):
            @abstractmethod
            def pay(self, amount):
                pass


        class OnlinePayment(Payment):
            def pay(self, amount):
                print(f"Payment of ₹{amount} completed successfully.")
                return True


        class RedBus:
            bus = {i: "Available" for i in range(1, 11)}

            def __init__(self, payment_method):
                self.payment_method = payment_method

            def display_seat(self):
                print("--------MVR Travels--------")
                for seat, status in self.bus.items():
                    print(seat, status)

            def booking(self, seatno, amount=500):
                if seatno not in self.bus or self.bus[seatno] != "Available":
                    print("Seat is already booked or invalid.")
                    return

                self.bus[seatno] = "Booked"
                print(f"Your seat {seatno} is reserved. Taking you to payment.")
                if not self.payment_method.pay(amount):
                    self.bus[seatno] = "Available"


        class User(RedBus):
            def display(self, name, email, phno):
                self.name, self.email, self.phno = name, email, phno
                print(f"Hello {name}, welcome to RED BUS")


        vivek = User(OnlinePayment())
        vivek.display("Vivek", "vivek@example.com", "9876543210")
        vivek.booking(4)
        vivek.display_seat()

