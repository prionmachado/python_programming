# Bank system using classes
class bank:
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.balance = balance

    def deposit(self,money):
        money = int(input("Enter amount to be Deposited: "))
        if money > 0:
            self.balance += money
            print( money,"deposited successfully.")
        else:
            print("Invalid amount.") 

    def withdraw(self,money):
        money = int(input("Enter amount to be Withdrawn: "))
        if self.balance>=money:
            self.balance-=money
            print(money,"withdrawn successfully")
        else:
            print("Not enough balance")

    def check_balance(self):
        print("Available Balance :",self.balance)

acc = bank(123,"Prion",100000)
acc.deposit(0)
acc.withdraw(0)
acc.check_balance() 