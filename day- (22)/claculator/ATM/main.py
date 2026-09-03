import logic as lg

if lg.login():
    lg.menu()

while True:
    choice = input("Enter your choice: ").lower()
    if choice == 'c':
        lg.check_balance()
    elif choice == 'd':
        lg.deposit()
    elif choice == 'w':
        lg.withdraw()
    elif choice == 'v':
        lg.view_history()
    elif choice == 'e':
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")