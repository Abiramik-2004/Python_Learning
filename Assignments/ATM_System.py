print("ATM System")
n=int(input("Enter the pin: "))
if(n==1234):
    print("Welcome to ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        print("Your balance is ",1000)
    elif(choice==2):
            amount=int(input("Enter the amount to deposit: "))
            if(amount<=0):
                print("Invalid amount")
            else:
                print("You have deposited" ,amount)
                print("Your new balance is",1000+amount)
    elif(choice==3):
        amount=int(input("Enter the amount to withdraw: "))
        if(amount>1000):
            print("Insufficient balance")
        else:
            print("You have withdrawn ",amount)
            print("Your new balance is",1000-amount)
    elif(choice==4):
        print("Thank you for using ATM")
    else:
        print("Invalid choice")
else:
    print("Invalid pin")