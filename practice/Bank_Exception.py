balance=int(input("Enter the balance amount: "))
withdrawl=int(input("Enter the amount you want to withdrawl: "))
if balance<withdrawl:
    try:
        raise ValueError("There is an Value error")
    except:
        print("Enter the Sufficient amount to withdraw")