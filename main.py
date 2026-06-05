from services.bank_service import bankservices

bank_service = bankservices()

while True:

    print("\n=====Banking=====System")

    print("1.Create Account")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == 1:
        try:

            account_number = int(
                input("Enter account number: ")
            )

            customer_name = input(
                "Enter Customer Name: "
            )

            balance = float(
                input(
                    "Enter opening balance: "
                )
            )

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

                        print("Program closed")

                        break
                    else

                    print("Invalid Choice")
