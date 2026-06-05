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


def find_account(self, account_number):

    for account in self.account:

        if account.account_number == account_number:
            return account

        return None


def deposit_money(self, account_number, amount):
    account = self.find_account(account_number)

    if account is not None:

        account.deposit(amount)

        return True

    return False

def withdraw_money(self, account_number,amount):

    account = self.find_account(account_number)

    if account is not None:

        return account.withdraw(amount)

    return None

def check_balance(self, account_number):
    account = self.find_account(account_number)

    if account is not None:
        return account.get_balance()

    return None
    