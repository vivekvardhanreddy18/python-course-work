data = {
    123456:{'name':"Vivek",'pin':1234,'balance':10000,'history':[]},
    789012:{'name':"vinith",'pin':5678,'balance':15000,'history':[]},
    342354:{'name':"rushikesh",'pin':9012,'balance':20000,'history':[]},
    163777:{'name':"karthik",'pin':3456,'balance':25000,'history':[]},
}

def login():
    global acc_num
    acc_num = int(input("Enter your account number: "))
    pin = int(input("Enter your PIN: "))
    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login successful!\n\nWelcome, ", data[acc_num]['name'])
        return True
    else:
        print("Invalid credentials.")
        return False
def menu():
    print("\nMenu:")
    print("[C]heck Balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[V]iew Transaction History")
    print("[E]xit")

def check_balance():
    print("Your current balance is: ", data[acc_num]['balance'])

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    data[acc_num]['balance'] += amount
    data[acc_num]['history'].append((amount , "is deposited"))
    print("Amount deposited successfully!\nYour new balance is: ", data[acc_num]['balance'],"\n\n")

def withdraw():
    amount = float(input("Enter the amount to withdraw: "))
    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance'] -= amount
        data[acc_num]['history'].append((amount , "is withdrawn"))
        print("Amount withdrawn successfully!\nYour new balance is: ", data[acc_num]['balance'],"\n\n")
    else:
        print("Insufficient balance.")

def view_history():
    if data[acc_num]['history']:
        print("============Transaction History============")
        for i in data[acc_num]['history']:
            print(i)
        print("============End of history============")
    else:
        print("No transaction history available.")