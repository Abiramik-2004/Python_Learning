print("------Personal Expense Tracker------")
print("------------------------------------")
list={}
Amount=0
while True:
    print("1. Add Income")
    print("2. Add Expenses")
    print("3. Display all the expense list")
    print("4. Calculate total expenses")
    print("5. Calculate remaining balance")
    print("6. Exit")
    
    choice=int(input("Enter the Choice: "))
    if choice==1:
        n=int(input("Enter your income: "))
        Amount=n
        print("Your Income is : ",Amount)
    elif choice==2:
        exp_name=input("Enter the expense name: ")
        exp_amount=int(input("Enter the amount it needs"))
        list[exp_name]=exp_amount
    elif choice==3:
        for i,j in list.items():
            print(i,"  -  ",j)
    elif choice==4:
        count=0
        for i, j in list.items():
            count+=j
        print(count)
    elif choice==5:
        count=Amount
        for i, j in list.items():
            count-=j
        print("The remaining balance - ",count)
    elif choice==6:
        break;
    else:
        print("Enter the valid choice")


