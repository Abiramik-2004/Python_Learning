Employee = {
        1:("Abirami", "Developer", 30000),
        2:("Bhaskar", "Tester", 25000),
        3:("Priya", "Associate Engineer", 28000),
        4:("Prasana", "Manager", 50000)
}

while True:
    print("1.Display Employees")
    print("2.Search Employee")
    print("3.Highest Salary Employee")
    print("4.Lowest Salary Employee")
    print("5.Add Employee")
    print("6. Remove Employee")
    print("7.Exit")
    choice = int(input("Enter your choice "))
    if choice == 1:
        for i,j in Employee.items():
            print(i,j[0],j[1])
    elif choice == 2:
        employee_id = int(input("Enter employee ID: "))
        found = False
        for i,j in Employee.items():
            if(i==employee_id):
                print(i,j[0],j[1])
                found=True
                break
        if found == False:
            print("Employee is not found")
    elif choice == 3:
        top = max(Employee,key=lambda c:Employee[c][1])
        print(top)
    elif choice == 4:
        low = min(Employee,key=lambda c:Employee[c][1])
        print(low)
    elif choice == 5:
        Employee_id = int(input("Enter Employee ID "))
        Employee_name = input("Enter Employee Name ")
        Employee_role = input("Enter Employee Role ")
        Employee_salary = int(input("Enter Employee Salary "))
        Employee[Employee_id]=(Employee_name,Employee_salary)
        print("Employee added")
    elif choice == 6:
        code=int(input("Enter the employee id"))
        Employee.pop(code)
        print("Employee deleted")
    elif choice == 7:
        break
    else:
        print("Invalid one")