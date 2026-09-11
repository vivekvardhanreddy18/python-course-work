class redbus:
    bus={i: "Available" for i in range(1,11)}

    def displayseat(x):
        print("--------MVR Travels--------")
        for i in redbus.bus:
            print(i,redbus.bus[i])

    def booking(x,seatno):
        for i in redbus.bus:
            if i==seatno and redbus.bus[i]=='Available':
                redbus.bus[i] = 'Booked'
                print(f"Your {seatno} is successfully booked")
                break
        else:
            print("Seat is already booked")

class user(redbus):
    def dispaly(x,name,email,phno):
        x.name = name
        x.email = email
        x.phno = phno
        print("f'Hello {name} , Welcome to MVR Travels")








vivek = redbus()
vivek.booking(4)
vivek.displayseat()

        