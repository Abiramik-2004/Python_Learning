l=[10,20,10,30,20,40,50,30]
s=set()
for n in l:
    if n in s:
        print(n)
    else:
        s.add(n)

'''
student class we having constructor in that name and marks, sum of marks and avg marks
'''
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.mark=marks
    def sum(self):
        return sum(self.mark)
    def avg(self):
        return sum(self.mark)/len(self.mark)

student1=Student("Abirami",[85,90,78,99,98])
print("Total: ",student1.sum())
print("avg: ",student1.avg())