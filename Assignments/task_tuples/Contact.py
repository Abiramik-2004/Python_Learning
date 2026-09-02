Contact = (
        (1, "Abirami", "9876543210"),
        (2, "Anisha", "9876543211"),
        (3, "Priya", "9876543212"),
        (4, "Bharani", "9876543213")
)

while True:
    print("1.Display Contacts")
    print("2.Search Contact")
    print("3.Add Contact")
    print("4.Exit")

    choice = int(input("Enter your choice "))

    if choice == 1:
        for i in Contact:
            print(i)

    elif choice == 2:
        contact_id = int(input("Enter Contact ID: "))
        found = False
        for i in Contact:
            if i[0] == contact_id:
                print(i)
                found = True
                break
        if found == False:
            print("Contact is not found")
    elif choice == 3:
        Contact_id = int(input("Enter Contact ID "))
        Contact_name = input("Enter Contact Name ")
        Contact_number = input("Enter Contact Number ")

        Contact += ((Contact_id, Contact_name, Contact_number),)

        print("Contact added")
    elif choice == 4:
        break
    else:
        print("Invalid one")