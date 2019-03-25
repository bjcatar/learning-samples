class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """This class generates checking accounts objects"""

    type="checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

### Jack
jack_checking = Checking("jack_balance.txt", 1)
print(jack_checking.balance)

jack_checking.transfer(100)
#jack_checking.deposit(100)
jack_checking.commit()

print(jack_checking.balance)
print(jack_checking.type)

### John
john_checking = Checking("john_balance.txt", 1)
print(john_checking.balance)

john_checking.transfer(100)
#john_checking.deposit(100)
john_checking.commit()

print(john_checking.balance)
print(john_checking.type)

print(john_checking.__doc__)
