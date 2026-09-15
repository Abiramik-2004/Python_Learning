class BankAccount:
    def __init__(self,name,acc_num,balance):
        self.__name=name
        self.__accountno=acc_num
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("Money deposited successfully....")
        else:
            print("Invalid amount")
    def withdrawl(self,amount):
        if amount>0 and amount<self.__balance:
            self.__balance-=amount
            print("Money withrawn successfully....")
        else:
            print("Insufficient or invalid money..")
    def checkbalance(self):
        print("Your baance is ",self.__balance)
    def accountDetails(self):
        print("Name :",self.__name)
        print("Account Number :",self.__accountno)
        print("Balance :",self.__balance)

class SavingAccount(BankAccount):
    def withdrawl(self, amount):
        super().withdrawl(amount)

class CurrentAccount(BankAccount):
    def withdraw(self,amount):
        print("Curent Account withdrawl....")
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print("Amount wihdrawn successfully...")
        else:
            print("Withdrawl limit exceeded...")

name=input("Enter your name: ")
acc_num=input("Enter account number: ")
print("1. Saving account")
print("2.Current account")
account_type=int(input("Enter account type: "))
balance=input("ENter balance: ")
if account_type==1:
    account=SavingAccount(name,acc_num,balance)
elif account_type==2:
    account=CurrentAccount(name,acc_num,balance)
else:
    print("Invalid account type")

while True:
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check balance")
    print("4.Display Account details")
    print("5.Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        amount=int(input("Enter the amount: "))
        account.deposit(amount)
    elif choice==2:
        amount=int(input("Enter the amount: "))
        account.withdrawl(amount)
    elif choice==3:
        account.checkbalance()
    elif choice==4:
        account.accountDetails()
    elif choice==5:
        break
    else:
        print("Invalid Choice...")
