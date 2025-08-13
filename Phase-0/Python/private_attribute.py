class Account:
    ## constructor to initialize account details
    def __init__ (self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance

    ## Add the money to the account
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")
    
    ## Withdraw the monney from the account
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient Funds")

        ## Display the account details 
    def account_details(self):
            print(f"Account Number: {self.__account_number}, Balance: {self.__balance}")
        
if __name__ == '__main__':
    acc1 = Account("2333","priyam", 233444)

    acc1.withdraw(10000)
    acc1.deposit(3455)
    acc1.account_details()