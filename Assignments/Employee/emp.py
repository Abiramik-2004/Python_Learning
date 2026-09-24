import os

print(os.getcwd())

while True:
    print("1. Add Employee ")
    print("2. View Employee ")
    print("3. SearchEmployee ")
    print("4. Delete all Employee")
    print("5. Exit")
    option=int(input("Enter the Option: "))
    if option==1:
        emp_id=input("Enter the employee id: ")
        name=input("Enter the name of the Employee: ")
        dept=input("Enter the department: ")
        salary=input("Enter salary: ")
        fp=open("emp.txt","a")
        fp.write(emp_id + "," + name + "," + dept + "," + salary + "\n") 
        fp.close() 
        print("Employee saved successfully..")
    elif option==2:
        fp=open("emp.txt","r")
        data=fp.read()
        fp.close()
        if data:
            print("\nEmployee Records:")
            print(data)
        else:
            print("No employee records found")
    elif option==3:
        search=input("Enter Employee ID: ")
        fp=open("emp.txt","r")
        found=False
        for line in fp:
            if search.lower() in line.lower():
                print("\nEmployee found: ")
                print(line)
                found=True
        fp.close()
        if  found==False:
            print("Employee not found")
    elif option==4:
        confirm=input("Do you want to delete all the employee details")
        if confirm.lower()=="yes":
            fp=open("emp.txt","w")
            fp.write("")
            fp.close()
        else: 
            print("Delete operation cancelled.") 
    elif option == 5: 
        break 
    else: 
        print("Invalid option. Please try again.")
