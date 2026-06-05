from services.bank_service import bankservices

bank_service = bankservices()

bank_service.load_accounts()

while True:

    print("\n===== Banking System =====")

    print("1.Create Account")
    print("2.View All Accounts")
    print("3.Deposite money")
    print("4.Withdraw Money")
    print("5.Check balance")
    print("6.Delete Account")
    print("7.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            account_number = int(input("Enter account number: "))
            customer_name = input("Enter Customer Name: ")
            balance = float(input("Enter opening balance: "))

            account = bank_service.create_account(
                account_number,
                customer_name,
                balance
            )

            print("\nAccount created successfully")
            print(account.display_account())
        except ValueError:
            print("Invalid Input")
    elif choice == "2":
        accounts = bank_service.get_all_accounts()

        if len(accounts) == 0:
            print("\nNo accounts found.")
        else:
            print("\n====All Accounts===")
            for account in accounts:
                print(account.display_account())
                print("_" * 30)
    elif choice == "3":
        try:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))

            success = bank_service.deposit_money(
                account_number,
                amount
            )

            if success:
                print("Deposit successful")
            else:
                print("Account not found")
        except ValueError:
            print("Invalid input !")
    elif choice == "4":
        try:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))

            result = bank_service.withdraw_money(
                account_number,
                amount
            )

            if result is True:
                print("Withdrawal Successful")
            elif result is False:
                print("Insufficient Balance")
            else:
                print("Account Not Found")
        except ValueError:
            print("Invalid input!")
    elif choice == "5":
        try:
            account_number = int(input("Enter account number: "))

            balance = bank_service.check_balance(account_number)

            if balance is not None:
                print(f"Current Balance: {balance:.2f}")
            else:
                print("Account Not Found")
        except ValueError:
            print("Invalid input!")

    elif choice == "6":
        try:
            account_number = int(
                input("Enter account number: ")
            )

            success = bank_service.delete_account(
                account_number
            )

            if success:
                print("Account Deleted Successfully")
            else:
                print("Account Not Found")

        except ValueError:
            print("Invalid input!")

    elif choice == "7":

        print("Program closed")
        break
    else:
        print("Invalid Choice")
