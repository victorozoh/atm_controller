#!/usr/bin/env python3

class Bank:
    """
    Implements a simple Bank Class where Users/Customers
    can only operate Checking or Savings Accounts
    """
    def __init__(self, account_name='Foo', account_number='0000'):
        self.account_name = account_name
        self.account_number = account_number
        self.account = BaseAccount()

    def access_account(self, account_type):
        if account_type == 'Checking Account':
            self.account = CheckingAccount(account_type='Checking Account')
        elif account_type == 'Savings Account':
            self.account = SavingsAccount(account_type='Savings Account')



class BaseAccount:
    """
    This is the Account Base class from which other types
    of accounts inherit.
    """
    def __init__(self, account_type=None, pin='1111', card_number='123456'):
        self._balance = 0
        self.account_info = {'type': account_type,
                             'pin': pin,
                             'card_number': card_number}

    def see_balance(self):
        """
        This method returns a string
        displaying the balance on the account.
        """
        print("Balance on your account is {}".format(self._balance))

    def deposit(self, amount):
        """
        This method increases the balance
        on the account by the amount specified by User.
        """
        self._balance += amount
        print("You successfully deposited {}".format(amount))

    def withdraw(self, amount):
        """
        This method decrements the balance on the
        account by the amount specified by the User.
        """
        if amount < self._balance:
            self._balance -= amount
            return amount
        else:
            return "Amount entered exceeds balance. Please enter another amount"

    def __repr__(self):
        return "Base Account with balance: ".format(self._balance)


class CheckingAccount(BaseAccount):
    def __init__(self, account_type):
        super().__init__(self, account_type)

    def __repr__(self):
        return "Checking Account with balance: ".format(self._balance)


class SavingsAccount(BaseAccount):
    def __init__(self, account_type):
        super().__init__(self, account_type)

    def __repr__(self):
        return "Savings Account with balance: ".format(self._balance)


class Controller:
    """
    This class implements a simple Controller
    for a Bank ATM
    """
    def __init__(self, bank):
        self.bank = bank
        self.account_types = {"C": 'Checking Account', 'S': 'Savings Account'}

    def enter_pin(self, pin):
        if pin == bank.account.account_info['pin']:
            return True
        else:
            return False

    def insert_card(self, card_number):
        if card_number == bank.account.account_info['card_number']:
            return True
        else:
            return False

    def select_account(self, acc_type):
        bank.access_account(self.account_types[acc_type])



if __name__ == '__main__':
    # instantiate Bank object
    bank = Bank()
    # create ATM controller object
    controller = Controller(bank)

    # Test use of Controller to Access Account
    # Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
    # note: PIN and Card Number have been initialized to 1111 and 123456 in Account class
    # via default parameters

    print('Please insert card')
    if controller.insert_card('123456'):
        # If successful, ask for PIN
        print("Please enter your PIN")
        if controller.enter_pin('1111'):
            acc_type = input("Please select your account type. Type 'c' for Checking or 's' for Savings ")
            acc_type = acc_type.upper()
            controller.select_account(acc_type)
            # Proceed to display balance
            controller.bank.account.see_balance()
            # make a Deposit
            deposit = int(input("Please enter an integer dollar amount to deposit "))
            controller.bank.account.deposit(deposit)
            # display new Balance
            controller.bank.account.see_balance()
        else:
            print("Wrong PIN, please, enter PIN again...")
    else:
        print("Please insert card again...")
