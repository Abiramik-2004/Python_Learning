tasks=[]
print("1. Add the task")
print("2. View the task")
print("3. Remove the Task")
print("4. Count the task")
print("5. Exit task")

choice=int(input("Enter the task: "))

while True:
    if( choice==1):
        task=input("Enter a task: ")
        tasks.append(task)
        print("Task has been added")
    elif choice==2:
        if(len(tasks)==0):
            print("There is no task")
        else:
            print(tasks)
    elif choice==3:
        task=input("enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task is removed")
        else:
            print("Task not present")
    elif choice==4:
        print("No of task: ",len(tasks))
    else:
        exit(0)