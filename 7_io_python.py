print("a","b","c",sep=",")
print(10,20,30,sep="-")

print(10) #the print statement always moves the cursor from the newline
print(20)

print("python",end="->")
print("java",end="->")
print("cpp")

'''Taking multiple input
------------------------
Split Function: It is used to split the string into multiple parts
'''
# a,b,c=input("Enter the input: ").split()
# print(a)
# print(b)
# print(c)

name="Akil"
age=99
print("My name is ",name, "and i am",age," years")

'''Format String/ fstring
    -> format function: An f-string is an easy way to put variables and expressions inside a string.
    -> You write f before the string and put variables inside {}.
    '''
print(f"My name is {name} and i am {age} years old")
# print(f"My name is {} and i am {} years old")----it is not possible
print("My name is {0} and i am {1} years old".format(name,age))

'''
Take a word and display its:
first character
second character
last character
using fString
'''
