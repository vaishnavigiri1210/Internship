balance = 10000

while True:
    print("\n------ ATM MENU ------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Your current balance is ₹", balance)

        case 2:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Amount deposited successfully")
            print("Updated balance is ₹", balance)

        case 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Please collect your cash")
                print("Remaining balance is ₹", balance)
            else:
                print("Insufficient balance")

        case 4:
            print("Thank you for using ATM")
            break   # EXIT LOOP

        case _:
            print("Invalid choice")
