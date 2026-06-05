class BankAccount:
    def _init_(self, account_number, customer_name, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, ammount):
        self.ammount += ammount

    def withdraw(self,amount):
           if amount <= self.balance:
             self.balance -= amount
             return True

        return False

    def display_account(self):
        return(
            f"Account Number: {self.account_number}\n"
            f"Customer Name: {self.customer_name}\n"
            f"balance: {self.balance:.2f}"
            
        )
