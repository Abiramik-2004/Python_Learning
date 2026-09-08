from Calculator import *
def dispay_detail(name,marks):
    print("------Student Detail------")
    print("Student Name: ",name)
    for i in range(5):
        print(f"Subject {i+1}: ",marks[i])
    print("---------------------")
    print("Average: ",Average(marks))
    print("Total: ",total(marks))
    print("Pecentage: ",percentage(marks))
    print("Grade: ",grade(Average(marks)))