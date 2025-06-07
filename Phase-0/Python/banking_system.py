class Account:
    ## constructor to initialize account details
    def __init__ (self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    ## Add the money to the account
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    ## Withdraw the monney from the account
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient Funds")

        ## Display the account details 
        def account_details(self):
            print(f"Account Number: {self.account_number}, Balance: {self.balance}")
    
    ## Inheritance : SavingAccounts inherits from Account
class SavingsAccount(Account):
            def __init__(self, account_number, account_holder, balance, interest):
                super().__init__(account_number, account_holder, balance)
                self.interest = interest
        
        ## Polymorphism : Display the account details
            def account_details(self):
                print(f"Saving Account Number: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest}")
    
            def add_interest(self):
                interest = self.balance * self.interest / 100
                self.balance += interest
    
                print(f"Interset added : {interest}, New Balance: {self.balance}")

## Inheritance: CurrentAccount inherits from Account
## Overdraft Limit : An overdraft limit in a current acount is a pre-approved credit line that allows you to withdraw more money than your current balance, up to a limit
class CurrentAccount(Account):
            def __init__(self, account_number, account_holder, balance, overdraft_limit):
                super().__init__(account_number, account_holder, balance)
                self.overdraft_limit = overdraft_limit

            def withdraw(self, amount):
                if amount <= self.balance + self.overdraft_limit:
                    print(f"Withdraw {amount}, New balance: {self.balance}, Overdraft Limit : {self.overdraft_limit}")

            def account_details(self):
                print(f"Current Account: {self.account_number}, Balance: {self.balance} ")

if __name__ =='__main__':
    acc1 = SavingsAccount("SA123","prince", 10000, 3)
    acc2 = CurrentAccount("CA345", "priyam", 100000, 25000)

    acc1.deposit(20000)
    acc1.add_interest()
    acc1.account_details()
    
    acc2.deposit(50000)
    acc2.account_details()
    acc2.withdraw(125000)



        

    



