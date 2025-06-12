class Account:
    ## Constructor to initialize account details
    def __init__(self, account_number, account_holder, balance):
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

    ## Withdraw the money from the account
    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f"{amount} withdrawn")
        else:
            print("Insufficient Funds")
    
    ## Display the account details
    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

## Inheritance: SavingsAccount inherits from Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    ## Polymorphism: Display the account details
    def display(self):
        print(f"Savings account Number: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest_rate}%")

    ## Added the interest in the savings account
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")

## Inheritance: CurrentAccount inherits from Account
## Overdraft Limit: An overdraft limit in a current account is a pre-approved credit 
## line that allows you to withdraw more money than your current account balance, up to a certain limit
class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    ## Polymorphism: Overriding the withdraw method
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")
    
    ## Polymorphism: Overriding the display method
    def display(self):
        print(f"Current Account: {self.account_number}, Balance: {self.balance}, Overdraft Limit: {self.overdraft_limit}")

if __name__=='__main__':
    acc1 = SavingsAccount("SA123", "Priya Bhatia", 10000, 3)
    acc2 = CurrentAccount("CA345", "Shivani Gupta", 100000, 25000)

    acc1.deposit(20000)
    acc1.add_interest()
    acc1.display()
    
    acc2.deposit(50000)
    acc2.display()
    acc2.withdraw(125000)