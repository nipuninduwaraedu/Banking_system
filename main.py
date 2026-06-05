from services.bank_service import bankservices

bank_service = bankservices()

while True:

    print("\n===== Banking System =====")

    print("1.Create Account")
    print("2.View All Accounts")
    print("3.Exit")

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
        print("Program closed")
        break
    else:
        print("Invalid Choice")
