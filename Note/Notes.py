while True:
    print("Student Notes Manager")
    print("1. Add Notes")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Delete all the notes")

    option=int(input("Enter your choice: "))

    if option==1:
        note=input("Enter your note: ")
        fp=open("Notes.txt","a")
        fp.write(note+"\n")
        print("note saved successfully..")
    elif option==2:
        fp=open("Notes.txt","r")
        data=fp.read()
        print(data)
    elif option==3:
        fp=open("Notes.txt","r")
        search=input("Enter a word to search..")
        data=fp.read()
        fp.close
        if search in data:
            print("Found")
        else:
            print("Not found")
    else:
        confirm=input("Do you want to delete all the records..(yes/no)?")
        if confirm.lower()=="yes":
            fp=open("Notes.txt","w")
            fp.write("")
            print("All the notes has been deleted")
    
