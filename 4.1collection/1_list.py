# List

num=[1,3,5,'o']
print(num)
'''Getting the list from the users'''
'''There are serveral ways to get a list from the usser in python
        1.Enter numbers seprated by space 
        2.Items seprated by commas
        3. Enter one items at a time '''
items =list(map(int, input("Enter items separated by commas: ").split(",")))

print(items)

items =list(map(int, input("Enter items separated by spaces: ").split()))

print(items)

n = int(input("How many items? "))

items = []
for i in range(n):
    item = input(f"Enter item {i + 1}: ")
    items.append(item)

print(items)