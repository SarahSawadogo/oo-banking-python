# 1. Build a new class called `BankAccount`...
class BankAccount:
    def __init__ (self, name, type_of_account, balance, status, pin, banking_number, interest ):
        self.name = name 
        self.type_of_account = type_of_account
        self.balance = balance
        self.status = status

    def deposit(self, deposit): 
        self.balance += deposit

    def check_balance(self):
        return "Your current balance is " + str(self.balance)

    def is_valid(self):
        if self.status == "open":
            return True
        elif self.status == "closed" or self.status == "zero":
            return False
        

    pass # delete this line when you're ready to build the BankAccount class



#  ... and instantiate a new account for a user named "Kiran".
kiran_account = BankAccount("Kiran", "Bank Account", 1000, "open","3345", "510234567", "0.2%" )

# i. Confirm that Kiran's new account is of the type `BankAccount`.

print(kiran_account.type_of_account)

# ii. Confirm that the name on Kiran's account is "Kiran".
print(kiran_account.name)

# iii. Confirm that Kiran's account has a balance of $1000.
print(kiran_account.balance)

# iv. Confirm that Kiran's account is `open`.
print(kiran_account.status)

# v. Set Kiran's balance to $2000. Confirm his new account balance.
kiran_account.balance = 2000
print(kiran_account.balance)

# Now you're on your own to write tests for the rest...

print(kiran_account.deposit(300))

jonathan_account = BankAccount ("Savings", "Jonathan's Savings Account", 0, "open", 2345, "123456789", "0.2%")
print(jonathan_account.is_valid())

monica_account = BankAccount ("Checkings", "Monica's Checkings Acount", 100, "closed", 5567, "7890654", "0.2%")
print(monica_account.is_valid())

class Transfer:
    pass # delete this line when you're ready to build the Transfer class

