from details import *
name=input("Enter the Student Name: ")
marks =[]
for i in range(5):
    mark=int(input(f"Enter the mark for Subject{i+1}: "))
    marks.append(mark)
dispay_detail(name, marks)