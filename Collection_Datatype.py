'''
1. Python Collection Data Types
-------------------------------
    ✨List [ ]
    ● Ordered
    ● Mutable (can be modified)
    ● Allows duplicate values
    numbers = [1, 3, 5, "o"]

    ✨Tuple ( )
    ● Ordered
    ● Immutable (cannot be modified)
    t = (1, 2, 3)

    ✨Set { }
    ● Unordered
    ● No duplicate values
    s = {1}

    ✨Dictionary {key : value}
    Stores data as key-value pairs.
    student = {
    1: "One"
    }

_____________________________________________

2. Variable Naming Rules
-----------------------
✔ Valid Rules
● Variable should not begin with a digit

❌ Invalid
1abc = 10

✔ Valid
abc1 = 10
--------------------------
Cannot use Python Keywords
Invalid
if = 10
def = 20
int = 30
---------------------------
No Spaces Allowed
❌

my name = "Tech"
✔
my_name = "Tech"
---------------------------

No Special Characters
Allowed: '_'

Not Allowed
'@
#
$
%
&'

Example
abc_1 = 100 # Valid
@abc = 100 # Invalid
_______________________________________________
Case Sensitive
a = 10
print(a)
A = 20
print(A)
Output
10
20
a and A are different variables.
____________________________________________________________
3. Type Conversion
------------------
Python automatically converts one type into another when needed.

num1 = 10
num2 = 10.6
add = num1 + num2
print(add)
print(type(add))

Output
20.6
<class 'float'>
__________________________________________________________
7. Type Casting
----------------
Manually converting one data type into another.

x = 100.6

print(int(x))
print(float(x))
print(str(x))

Output
100
100.6
'100.6'
_________________________________________________________________
Examples:
-------
int("25")
Output
25

float("25")
Output
25.0

str(100)
Output
'100'

Invalid Conversion
int("print")
Output
ValueError
______________________________________________________________
4. Swapping Variables
---------------------
Method 1: Using Temporary Variable
a = 10
b = 20
c = a
a = b
b = c
print(a)
print(b)
Output
20
10

Method 2: Python Shortcut
a = 10
b = 20
a, b = b, a
print(a)
print(b)
Output
20
10
_________________________________________________________
5. Multiple Assignment
----------------------
Assign multiple values at once.
a, b = 1, 2
print(a)
print(b)

Output
1
2

Assign the same value to multiple variables.
a = b = c = 10
print(c)

Output
10
__________________________________________________
6. Arithmetic Example
a = 200
b = 300
c = a + b
print(c)

Output
500
__________________________________________________________

7. User Input
-------------
The input() function is used to take input from the keyboard.
a = input("Enter a number: ")
print(a)
Note: input() always returns a string.
To get an integer:
a = int(input("Enter a number: "))
To get a float:
a = float(input("Enter a decimal number: "))
_____________________________________________________________

12. Python IDEs
---------------
Common Python development environments:
● IDLE (Python's default IDE)
● PyCharm
● Visual Studio Code (VS Code)
● Google Colab
● IntelliJ IDEA (with Python plugin)
● Jupyter Notebook
● Spyder
__________________________________________________________________
13. Summary
-----------
Concept Example
Integer a = 10
Float b = 10.5
String c = "Python"
Boolean d = True
Complex e = 2 + 3j
List [1,2,3]
Tuple (1,2,3)
Set {1,2,3}
Dictionary {"id":101}
Type type(a)
Memory Address id(a)
Input input()
Integer Input int(input())
Float Input float(input())
Type Casting int(), float(),
str()
Swap a, b = b, a
Multiple Assignment a = b = c = 10'''
print(123)