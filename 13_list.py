#  ✨List [ ]
#     ● Ordered
#     ● Mutable (can be modified)
#     ● Allows duplicate values
#     numbers = [1, 3, 5, "o"]
#index: It is the position present in a list

l=[1,2]
h=[3,4]
print(l+h) #[1, 2, 3, 4]
print(l*3) #[1, 2, 1, 2, 1, 2]

l=[1,2,3,4,5,6,7,8]
max(l)
min(l)
sum(l)

l=[1,1,2,7,3,4,5,6,8]
l.append(9) # to add an element
l.extend([10,11]) # to add multiple element
l.insert(7,7) # to add a element at a particular position
print(l)
print(l.index(3)) # to return element at a particular position
l.remove(11) # to remove an element with a value
l.pop(9) # to remove an element based on index
print(l)
print(l.count(1)) # to count the occurences of a particular element
print(l.sort()) # to sort the list
print(l.reverse()) # to reverse the list
l.clear() # to delete all the element 
print(l)


