Employee={
    (101," Abirami","Devlopment",20000),
    (102,"Priya","Tester",25000),
    (103,"Vicky","Designer",28000),
    (104,"Kumar","Manager",50000)
}
while True:
    print("1. Display Employees")
    print("2. Search Employees")
    print("3. Highest Salary")
    print("4. Lowest Salary")
    print("5. Add employee")
    print("6. Remove employee")
    print("7. Exit")

    choice=int(input("Enter your choice: "))
    if(choice==1):
        for i in Employee:
            print(i)
    elif(choice==2):
        emp_id=int(input("Enter an employee id to search: "))
        found=False
        for i in Employee:
            if i[0]==emp_id:
                print(i)
                found=True
                break
        if(found==False):
            print("Employee id is not found")
    elif(choice==3):
        max_sal=max(Employee, key=lambda s: s[3])
        print(max_sal)
    elif(choice==4):
        min_sal=min(Employee, key=lambda s: s[3])
        print(min_sal)
    elif(choice==5):
        Emp_id=int(input("Enter the employee id: "))
        emp_name=input("Enter the name of the Employee: ")
        emp_designation=input("Enter the designation of the Employee: ")
        emp_salary=int(input("Enter the Salary of the Employee: "))

        Employee.add((Emp_id,emp_name,emp_designation,emp_salary))
        print("Employee has been added Sucessfully")
    elif(choice==6):
        emp_id=int(input("Enter the employee id to remove: "))
        found=False
        for i in Employee:
            if i[0]==emp_id:
                Employee.remove(i)
                print("Employee has been removed successfully")
        if(found==False):
            print("Employee id is not found")
    elif(choice==7):
        break
    else:
        print("Invalid choice")