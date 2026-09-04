Contact = {
        1:("Abirami", "9876543210"),
        2:("Anisha", "9876543211"),
        3:("Priya", "9876543212"),
        4:("Bharani", "9876543213")
}

while True:
    print("1.Display Contacts")
    print("2.Search Contact")
    print("3.Add Contact")
    print("4.Delete Contact")
    print("5.Exit")

    choice = int(input("Enter your choice "))

    if choice == 1:
        for i,j in Contact.items():
            print(i,j[0],j[1])

    elif choice == 2:
        code = int(input("Enter Contact ID: "))
        found = False
        for i,j in Contact.items():
             if(i==code):
                print(i,j[0],j[1])
                found=True
                break
        if(found==False):
            print("Course code not present")
    elif choice == 3:
        Contact_id = int(input("Enter Contact ID "))
        Contact_name = input("Enter Contact Name ")
        Contact_number = input("Enter Contact Number ")

        Contact[Contact_id]=(Contact_name,Contact_number)
        print("Contact added successfully")

        print("Contact added")
    elif(choice==4):
            code=int(input("Enter the Contact-id to delete"))
            Contact.pop(code)
            print("Deleted successfuly")
    elif choice == 5:
        break
    else:
        print("Invalid one")