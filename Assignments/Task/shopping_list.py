shopping_list=[]
while True:
    print("1. Add the item")
    print("2. View the item")
    print("3. Remove the item")
    print("4. Count the items")
    print("5. Exit ")
    choice=int(input("Enter the choice: "))
    if( choice==1):
        item=input("Enter a item: ")
        shopping_list.append(item)
        print("item has been added")
    elif choice==2:
        if(len(shopping_list)==0):
            print("There is no item in the list")
        else:
            print(shopping_list)
    elif choice==3:
        item=input("enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("item is removed")
        else:
            print("item not present")
    elif choice==4:
        print("No of items present in a list: ",len(shopping_list))
    else:
        exit(0)

