courses={
    101:("Computer Networking",2.5),
    102:("Microprocessor andMicrocontroller",3),
    103:("Theory of computation",4),
    104:("Database Management System",3),
    105:("Data Structures",3.5)
}
while True:
    print("1. Display the course")
    print("2. Search course")
    print("3. Highest credits")
    print("4. Lowest Credits")
    print("5. Add a new Couses")
    print("6. Remove courses")
    print("7.Exit")

    choice=int(input("Enter the choice: "))
    if(choice==1):
        for i,j in courses.items():
            print(i,j[0],j[1])
    elif(choice==2):
        code=int(input("Enter the course code"))
        found=False
        for i,j in courses.items():
            if(i==code):
                print(i,j[0],j[1])
                found=True
                break
        if(found==False):
            print("Course code not present")
    elif(choice==3):
        max_credit=max(courses,key=lambda c:courses[c][1])
        print(max_credit,courses.get(max_credit))
    elif(choice==4):
        min_credit=min(courses,key=lambda c:courses[c][1])
        print(min_credit,courses.get(min_credit))
    elif(choice==5):
        course_code=int(input("Enter the course"))
        course_name=input("Enter the course name: ")
        course_credit=input("Enter the course credit: ")
        courses[course_code]=(course_name,course_credit)
        print("Course added successfully")
    elif(choice==6):
        code=int(input("Enter the course code to delete"))
        courses.pop(code)
        print("Deleted successfuly")
    elif(choice==7):
        break
    else:
        print("Provide valid choice")
    