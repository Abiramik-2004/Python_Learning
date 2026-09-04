'''
    List:
        It is a collectin which is used to store multiple values together
        we can access the eleemts by index
        It is ordered, mutable and allow duplicates
        it supports indexing and slicing
        it can contin different datatype
    
    empty list
        l=[]

    Indexing
        n[0]

    Adding element:
    append()--adding values in a list
    insert(ind,val)--adding element based by giving key and value
    extend(l)--adding multiple elements through giving another list

    Removing element:
    remove(val)--remove element
    pop()--removes last element
    clear()--delete all the element
    del:
        del values[1]
    
    sort()--sorting element 
    sort(reverse=True)--sorting in descending order

    len()
    max()
    min()
    sum()
    reverse()


'''
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


