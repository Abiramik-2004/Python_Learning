Course=((1,"Data Structures and Algorithm",2.5),
        (2,"Database Management System",3),
        (3,"Networking",4),
        (4,"Cryptography",5))

while True:
    print("1.Display Courses")
    print("2.Search Course")
    print("3.Highest credit couses")
    print("4.Lowest cedit courses")
    print("5.Add Course")
    print("6. Exit")

    choice=int(input("enter your choice "))
    if choice==1:
        for i in Course:
            print(i)
    elif choice==2:
        code=int(input("enter course code:  "))
        found=False
        for i in Course:
             if i[0]==code:
                  print(i)
                  found=True
                  break
        if found==False:
             print("Course is not found")
    elif choice==3:
        top=max(Course, key =lambda s:s[2])
        print(top)
    elif choice==4:
            top=min(Course, key =lambda s:s[2])
            print(top)
    elif choice==5:
        Course_code=int(input("enter Course_Code "))
        Course_name=input("enter the name of the Course ")
        Couse_credit=int(input("enter course credit"))

        Course+=tuple((Course_code,Course_name,Couse_credit),)
        print("Course added")
    elif choice==6:
        break
    else:
         print("Invalid one")
    