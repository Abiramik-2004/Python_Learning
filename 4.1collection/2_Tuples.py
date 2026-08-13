'''
Tuples:
-------
    ● Ordered
    ● Immutable (cannot be modified)

Creation of Tuples:
    
 '''

num=(1,2,3,4)
print(num)

items=tuple(map(int,input("Enter the items with space").split()))
print(items)

items=tuple(map(int,input("Enter the items with commas: ").split(',')))
print(items)
'''
You cannot use .append() directly on a tuple because tuples are immutable in Python.
num=()
n=int(input("Enter the number of item? "))
for i in range(n):
    item = input(f"Enter item {i + 1}: ")
    num.append(item)
print(num)
'''
# But we can convert the list into tuples
num=[]
n=int(input("Enter the number of items? "))
for i in range(n):
    item=input(f"Enter item {i + 1}:")
    num.append(item)
num=tuple(num)
print(num)

# Here is some program which is we cant modify the tuples so here is the program to create new tuple each of the time modification is maded
num = ()

n = int(input("Enter the number of items: "))

for i in range(n):
    item = input(f"Enter item {i + 1}: ")
    num = num + (item,)

print(num)