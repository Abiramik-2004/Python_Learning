'''
Dictionary
----------
    A dictionary ia a data Structure and it is used to store information in key-value pairs.
    A Dictionary stores data using unique keys and their corresponding values.
    It is ordered
    It can have duplicate values but not duplicated keys
    It is mutable

Creation of Dictionary
-----------------------
    # Using dict()
    # Using {}

Accessing Values
-----------------
    # Using[]
    # get()

Adding a new item:
------------------
    var_name[Key]=value
    
Updating a value:
-----------------
     var_name[Key]=value
   
Get method in dictionary:
    get()--get the value by key
    keys()--get all the keys in a dictionary
    values()--get all the values in a dictionary
    items()--get keys and values together

update or add the items
    update()-- to update single or multiple elements

Remove element
    pop()--remove specific item
    popitem()--remove last item
    clear()--remove all item

copy()--copy a dictionary
setdefault()--getorset the default value
fromkeys()--createa dictionary fromkey
len()--count items

in--check if the key exists
not in--check if a key doesn't exist
del--delete an item or dictionary

'''
# Creation of Dictionary
#Using {}

student={
    "name":"Abirami",
    "age":22
}
#Using dict()

std=dict(name="Abirami", age=22)

print(student)
print(std)

# Getting value from the dictionary
dict={
    1:"Chennai",
    2:"Vellore",
    3:"Trichy",
    4:"Ramanathapuram",
    5:"Karaikudi"
}
# get the value from key
for i in dict:
    print(dict.get(i))

# get all the keys
print(dict.keys())

# get all the values
print(dict.values())

#get all the items 
print(dict.items())

dict.update({6:"Dehradun"})
print(dict)


# get the value by using []
print(dict[1])

for i in dict:
    print(dict.get(i))

# Updating the value or Adding the value manually
dict[5]="Karaikal"
dict[7]="Karaikudi"
print(dict)
print(len(dict))
dict.setdefault(1,"Unknown")
print(dict[1])

# Removing the element from the dictionary
print(dict.pop(1))
print(dict.popitem())
del dict[2]
print(dict)
dict.clear()
print(dict)

