class BankAccount:
    def __init__(self, holder_name, initial_balance):
        self.holder_name = holder_name
        self.__balance = initial_balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f" {amount} TK deposit sucessfullly")
        else:
            print("Wrong Amount, Please give Real Amount.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Sorry! you do not have  sufficient Balance")
        elif amount <= 0:
            print("Please write real  amount")
        else:
            self.__balance -= amount
            print(f"sucessfully {amount} tk withdraw")

    def show_balance(self):
        print(f"👤 Account Holder: {self.holder_name}")
        print(f"💰 Current Balance: {self.__balance} TK")


my_account = BankAccount("Hamza", 1000)

my_account.show_balance()
print("-" * 30)


my_account.deposit(500)
my_account.show_balance()
print("-" * 30)

my_account.withdraw(2000) 
print("-" * 30)

my_account.withdraw(700)
my_account.show_balance()