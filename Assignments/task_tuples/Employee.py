Employee = (
        (101, "Abirami", "Developer", 30000),
        (102, "Bhaskar", "Tester", 25000),
        (103, "Priya", "Associate Engineer", 28000),
        (104, "Prasana", "Manager", 50000)
)

while True:
    print("1.Display Employees")
    print("2.Search Employee")
    print("3.Highest Salary Employee")
    print("4.Lowest Salary Employee")
    print("5.Add Employee")
    print("6.Exit")
    choice = int(input("Enter your choice "))
    if choice == 1:
        for i in Employee:
            print(i)
    elif choice == 2:
        employee_id = int(input("Enter employee ID: "))
        found = False
        for i in Employee:
            if i[0] == employee_id:
                print(i)
                found = True
                break
        if found == False:
            print("Employee is not found")
    elif choice == 3:
        top = max(Employee, key=lambda s: s[3])
        print(top)
    elif choice == 4:
        top = min(Employee, key=lambda s: s[3])
        print(top)
    elif choice == 5:
        Employee_id = int(input("Enter Employee ID "))
        Employee_name = input("Enter Employee Name ")
        Employee_role = input("Enter Employee Role ")
        Employee_salary = int(input("Enter Employee Salary "))
        Employee += ((Employee_id, Employee_name, Employee_role, Employee_salary),)
        print("Employee added")
    elif choice == 6:
        break
    else:
        print("Invalid one")