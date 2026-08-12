'''
Python Operators
-----------------
An operator is a symbol or keyword used to perform an operation on values or variables.

Example:
a = 10
b = 5
print(a + b)
Output:
15

1. Arithmetic Operators
-----------------------
Arithmetic operators are used to perform mathematical calculations.
Operator Name Example
+ Addition 10 + 5
- Subtraction 10 - 5
* Multiplication 10 * 5
/ Division 10 / 5
// Floor Division 10 //
3
% Modulus 10 % 3
** Exponentiation 2 ** 3
Program
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)
Output
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor Division: 3
Modulus: 1
Power: 1000

2. Relational / Comparison Operators
------------------------------------
Comparison operators compare two values. The result is always True or False.
Operator Meaning
== Equal to
!= Not equal to
> Greater than
< Less than
>= Greater than or equal
to
<= Less than or equal to
Program
a = 10
b = 20
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater:", a > b)
print("Less:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)
Output
Equal: False
Not Equal: True
Greater: False
Less: True
Greater or Equal: False
Less or Equal: True

3. Assignment Operators
------------------------
Assignment operators are used to assign and update values.
Operator Example Equivalent
= x = 10 x = 10
+= x += 5 x = x +
5
-= x -= 5 x = x -
5
*= x *= 5 x = x *
5
/= x /= 5 x = x /
5
//= x //=
5
x = x //
5
%= x %= 5 x = x %
5
**= x **=
5
x = x **
5
Program
x = 10
print("Initial:", x)
x += 5
print("After += :", x)
x -= 3
print("After -= :", x)
x *= 2
print("After *= :", x)
x /= 4
print("After /= :", x)
Output
Initial: 10
After += : 15
After -= : 12
After *= : 24
After /= : 6.0

4. Logical Operators
---------------------
Logical operators are used to combine multiple conditions.
There are three logical operators:
● and
● or
● not
and
Returns True only when both conditions are True.
age = 25
salary = 30000
print(age >= 18 and salary >= 25000)
Output:
True
or
Returns True when at least one condition is True.
age = 16
has_permission = True
print(age >= 18 or has_permission)
Output:
True
not
Reverses the result.
x = True
print(not x)
Output:
False
Complete Program
age = 25
salary = 30000
print("AND:", age >= 18 and salary >= 25000)
print("OR:", age >= 18 or salary >= 50000)
print("NOT:", not(age >= 18))
5. Bitwise Operators
Bitwise operators work with numbers at the binary level.
Operator Name
& Bitwise AND
| Bitwise AND
^ Bitwise XOR
~ Bitwise NOT
Program
a = 5
b = 3
print("AND:", a & b)
print("OR:", a | b)
Binary Explanation
5 = 101
3 = 011
AND:
101
011
---
001 = 1
OR:
101
011
---
111 = 7
Output:
AND: 1
OR: 7

6. Membership Operators
-----------------------
Membership operators check whether a value exists in a sequence such as a list, tuple, string,
set, or dictionary.
Two operators:
● in
● not in
Program
numbers = [10, 20, 30, 40, 50]
print(30 in numbers)
print(100 in numbers)
print(100 not in numbers)
Output:
True
False
True
String Example
name = "Python"
print("P" in name)
print("z" in name)
print("Java" not in name)
Output:
True
False
True

7. Identity Operators
---------------------
Identity operators check whether two variables refer to the same object in memory.
Two operators:
● is
● is not
Program
a = [10, 20, 30]
b = a
c = [10, 20, 30]
print(a is b)
print(a is c)
print(a is not c)
Output:
True
False
True
Why?
b = a
Both a and b refer to the same list object.
But:
c = [10, 20, 30]
creates another list object.
Even though the values are the same:
a == c
is True, but:
a is c
is False.
Important Difference
== → compares values
is → compares object identity'''
print("Operators in python")