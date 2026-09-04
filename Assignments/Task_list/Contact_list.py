Contacts=[]
while True:
    print("1. Add the phone number")
    print("2. View the Phone numbers")
    print("3. Remove the phone number")
    print("4. Count the Phone numbers")
    print("5. Exit ")
    choice=int(input("Enter the choice: "))
    if( choice==1):
        Phone_Number=input("Enter a Number: ")
        Contacts.append(Phone_Number)
        print("item has been added")
    elif choice==2:
        if(len(Contacts)==0):
            print("There is no Number  in the list")
        else:
            print(Contacts)
    elif choice==3:
        Phone_Number=input("enter the Number to remove: ")
        if Phone_Number in Contacts:
            Contacts.remove(Phone_Number)
            print("Number is removed")
        else:
            print("Number not present")
    elif choice==4:
        print("No of Phone Numbers present in a list: ",len(Contacts))
    else:
        exit(0)

