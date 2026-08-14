'''
Python Variables and Data Types –
Variables
What is a Variable?
A variable is a reserved memory location used to store data. It acts as a container that holds a
value, which can change during program execution.
A = 6
Here,
● A → Variable name
● 6 → Value stored in the variable
2. Creating Variables
Python automatically determines the data type based on the assigned value.
a = 6 # Integer
b = 22.4 # Float
c = "tech" # String
d = True # Boolean
e = 1 + 8j # Complex Number
3. Checking Variable Information
id()
Returns the memory address (identity) of the object.
a = 10
print(id(a))
type()
Returns the data type of the variable.
print(type(a))
Output
<class 'int'>
'''
a=10
print(id(a))
print(type(a))

