from models.bank_account import BankAccount


class bankservices:
    def __init__(self):
        self.account = []

    def create_account(self, account_number, customer_name, balance):

        account = BankAccount(
            account_number,
            customer_name,
            balance
        )


self.account.append(account)

return account

def get_all_accounts(self):
    return self.accounts