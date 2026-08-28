'''
1.List operations 
Create a list of 5 numbers. Add one number, sort the list,reverse it, and print the final list
'''
l=[30,20,50,40,10]
l.append(60)
print(l)
l.remove(10)
print(l)
l.sort()
print(l)
l.reverse()
print(l)

''' 
2. List of names
create a list of names. Add a new name, removwe a name, and  check whether " Ravi" exists in the list
'''
name=["Abi","Bhaskar","sathya","Chinna","Naathan","Ravi"]
name.append("Kavin")
name.remove("Naathan")
print(name)

if "Ravi" in name:
    print("Ravi is present in the list")
else:
    print("Not present in the list")


'''
3. Count Duplicates element
create a list containing duplicate numbers and find how many times a particular number occurs using count()

'''
l=[1,2,2,3,2,4,5,6,7,8,1]
for i in set(l):
    print(i,"->",l.count(i))