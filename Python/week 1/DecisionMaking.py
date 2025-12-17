balance = 5000

while True:
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amt = int(input("Enter amount to deposit: "))
        balance = balance + amt
        print("Money added")

    elif choice == 3:
        amt = int(input("Enter amount to withdraw: "))
        if amt <= balance:
            balance = balance - amt
            print("Please collect money")
        else:
            print("Not enough balance")

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Wrong choice")