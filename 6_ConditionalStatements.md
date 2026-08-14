Python Conditional Statements —
Complete Notes with Codes
1. Introduction
Conditional statements are used in Python to make decisions.
They allow a program to execute different blocks of code depending on whether a condition is
True or False.
Types of conditional statements
1. if statement
2. if-else statement
3. Nested if
4. if-elif-else
5. Conditional expression (ternary operator)
2. if Statement
The if statement executes a block of code when the given condition is True.
Syntax
if condition:
statement
Example 1
age = 20
if age >= 18:
print("You are eligible to vote.")
Output:
You are eligible to vote.
Example 2 — Check positive number
num = 10
if num > 0:
print("Positive number")
Output:
Positive number
Example 3 — Check even number
num = 12
if num % 2 == 0:
print("Even number")
Output:
Even number
Important point
If the condition is False, the if block is skipped.
age = 15
if age >= 18:
print("Eligible")
Output:
# No output
3. if Statement with User Input
The input() function can be used to take values from the user.
age = int(input("Enter your age: "))
if age >= 18:
print("You are eligible to vote.")
Output:
Enter your age: 20
You are eligible to vote.
Explanation
● input() takes input as a string.
● int() converts it into an integer.
● age >= 18 checks the condition.
● If it is True, the message is printed.
4. Multiple if Statements
We can use more than one if statement in a program.
Each if condition is checked independently.
Example
age = 65
if age >= 18:
print("You are an adult.")
if age >= 60:
print("You are a senior citizen.")
if age >= 80:
print("You are a very senior citizen.")
Output:
You are an adult.
You are a senior citizen.
The third condition is false, so its message is not printed.
Important
Multiple if statements can execute multiple blocks.
5. if-else Statement
The if-else statement is used when there are two possible outcomes.
● If the condition is True, the if block executes.
● If the condition is False, the else block executes.
Syntax
if condition:
statement1
else:
statement2
Example
age = 16
if age >= 18:
print("Eligible to vote.")
else:
print("Not eligible to vote.")
Output:
Not eligible to vote.
6. Check Even or Odd
This is one of the most common examples of if-else.
num = int(input("Enter a number: "))
if num % 2 == 0:
print("Even number")
else:
print("Odd number")
Output:
Enter a number: 7
Odd number
Explanation
The % operator gives the remainder.
For an even number:
number % 2 = 0
For an odd number:
number % 2 != 0
7. Check Positive or Negative
num = int(input("Enter a number: "))
if num >= 0:
print("Positive number")
else:
print("Negative number")
Output:
Enter a number: -5
Negative number
Note: With this code, 0 is treated as non-negative. If you want to classify zero
separately, use if-elif-else.
8. Check Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
print("A is greater")
else:
print("B is greater or equal")
Example
Enter first number: 25
Enter second number: 15
A is greater
9. Nested if Statement
A nested if is an if statement placed inside another if statement.
Syntax
if condition1:
if condition2:
statement
else:
statement
else:
statement
Example
marks = int(input("Enter your marks: "))
if marks >= 40:
if marks >= 75:
print("Passed with distinction")
else:
print("Passed")
else:
print("Failed")
Output
Enter your marks: 80
Passed with distinction
How it works
First:
if marks >= 40:
is checked.
If it is True, Python checks:
if marks >= 75:
Therefore, two conditions are checked one after another.
10. Nested if — Login Example
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
if password == "1234":
print("Login successful")
else:
print("Incorrect password")
else:
print("Invalid username")
Output
Enter username: admin
Enter password: 1234
Login successful
11. if-elif-else Statement
The if-elif-else statement is used when there are multiple conditions.
Syntax
if condition1:
statement1
elif condition2:
statement2
elif condition3:
statement3
else:
statement4
Python checks conditions from top to bottom.
When it finds the first True condition, it executes that block and skips the remaining conditions.
12. Grade Program
marks = int(input("Enter your marks: "))
if marks >= 90:
print("Grade A")
elif marks >= 80:
print("Grade B")
elif marks >= 70:
print("Grade C")
elif marks >= 60:
print("Grade D")
elif marks >= 40:
print("Grade E")
else:
print("Fail")
Output
Enter your marks: 85
Grade B
Why is it Grade B?
Python checks:
85 >= 90 → False
85 >= 80 → True
Therefore, it prints Grade B and stops checking the remaining conditions.
13. Temperature Example
temperature = int(input("Enter temperature: "))
if temperature >= 30:
print("It is hot.")
elif temperature >= 20:
print("It is warm.")
elif temperature >= 10:
print("It is cool.")
else:
print("It is cold.")
Output
Enter temperature: 25
It is warm.
14. Check Positive, Negative, or Zero
This is a very important if-elif-else example.
num = int(input("Enter a number: "))
if num > 0:
print("Positive")
elif num < 0:
print("Negative")
else:
print("Zero")
Output
Enter a number: 0
Zero
15. Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
print("A is largest")
elif b >= a and b >= c:
print("B is largest")
else:
print("C is largest")
Example
Enter first number: 25
Enter second number: 40
Enter third number: 15
B is largest
16. Voting Eligibility
age = int(input("Enter your age: "))
if age >= 18:
print("You are eligible to vote.")
else:
print("You are not eligible to vote.")
Output
Enter your age: 17
You are not eligible to vote.
17. Logical Operators in Conditions
Python provides three important logical operators:
Operator Meaning
and Both conditions must be True
or At least one condition must be
True
not Reverses the result
and Operator
Both conditions must be true.
age = 25
citizen = True
if age >= 18 and citizen:
print("Eligible to vote")
Output:
Eligible to vote
or Operator
At least one condition must be true.
day = "Sunday"
if day == "Saturday" or day == "Sunday":
print("Weekend")
Output:
Weekend
not Operator
The not operator reverses a Boolean value.
is_raining = False
if not is_raining:
print("You can go outside.")
Output:
You can go outside.
18. Comparison Operators
Comparison operators are frequently used with conditional statements.
Operator Meaning Example
== Equal to a == b
!= Not equal to a != b
> Greater than a > b
< Less than a < b
>= Greater than or equal
to
a >= b
<= Less than or equal to a <= b
Example
a = 10
b = 20
if a < b:
print("a is smaller than b")
Output:
a is smaller than b
19. Membership Operators
in and not in can also be used in conditions.
in
fruits = ["apple", "banana", "mango"]
if "apple" in fruits:
print("Apple is available.")
Output:
Apple is available.
not in
fruits = ["apple", "banana", "mango"]
if "orange" not in fruits:
print("Orange is not available.")
Output:
Orange is not available.
20. Identity Operators
Python has two identity operators:
● is
● is not
They check whether two references point to the same object.
a = None
if a is None:
print("a has no value")
Output:
a has no value
Important
Do not normally use is to compare ordinary values:
# Use this
if x == 10:
print("Ten")
rather than:
# Avoid this for value comparison
if x is 10:
print("Ten")
21. Boolean Values
A condition generally evaluates to either:
True
or
False
Example:
x = 10
print(x > 5)
print(x < 5)
Output:
True
False
These Boolean results can be used directly in if.
x = 10
if x > 5:
print("Condition is True")
22. Truthy and Falsy Values
Python allows many values to be used directly as conditions.
Falsy values include:
False
None
0
0.0
""
[]
()
{}
Example:
name = ""
if name:
print("Name entered")
else:
print("Name is empty")
Output:
Name is empty
A non-empty string is generally truthy:
name = "Rahul"
if name:
print("Name entered")
Output:
Name entered
23. Conditional Expression / Ternary
Operator
Python provides a short form of if-else.
Syntax
value_if_true if condition else value_if_false
Example
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
Output:
Adult
Another Example
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)
Output:
Odd
24. pass in Conditional Statements
Sometimes you may want to leave a block empty temporarily. Python requires a statement
inside the block, so you can use pass.
age = 20
if age >= 18:
pass
else:
print("Minor")
pass does nothing; it simply acts as a placeholder.
25. Nested if vs if-elif-else
Nested if
Used when one condition depends on another.
if age >= 18:
if has_id:
print("Entry allowed")
if-elif-else
Used when choosing between several alternatives.
if marks >= 90:
print("A")
elif marks >= 60:
print("B")
else:
print("C")
26. Important Rules of Python Conditional
Statements
Rule 1: Use a colon
if age >= 18:
print("Adult")
The : after the condition is compulsory.
Rule 2: Use indentation
Correct:
if age >= 18:
print("Adult")
Incorrect:
if age >= 18:
print("Adult")
Rule 3: else does not have a condition
Correct:
if x > 0:
print("Positive")
else:
print("Not positive")
Rule 4: elif must come after if
Correct:
if x > 10:
print("Greater")
elif x == 10:
print("Equal")
Rule 5: else must come at the end
if condition1:
...
elif condition2:
...
else:
...
27. Common Errors
Error 1: Forgetting :
Wrong:
if age >= 18
print("Adult")
Correct:
if age >= 18:
print("Adult")
Error 2: Incorrect indentation
Wrong:
if age >= 18:
print("Adult")
Correct:
if age >= 18:
print("Adult")
Error 3: Using = instead of ==
= is used for assignment.
== is used for comparison.
Wrong:
if age = 18:
print("Age is 18")
Correct:
if age == 18:
print("Age is 18")
28. Real-Life Example — Electricity Bill
units = int(input("Enter electricity units: "))
if units <= 100:
bill = units * 2
elif units <= 200:
bill = units * 3
else:
bill = units * 5
print("Electricity bill:", bill)
Example Output
Enter electricity units: 250
Electricity bill: 1250
29. Real-Life Example — ATM Withdrawal
balance = 5000
amount = int(input("Enter withdrawal amount: "))
if amount <= 0:
print("Invalid amount")
elif amount > balance:
print("Insufficient balance")
else:
balance = balance - amount
print("Withdrawal successful")
print("Remaining balance:", balance)
Example Output
Enter withdrawal amount: 2000
Withdrawal successful
Remaining balance: 3000
30. Real-Life Example — Simple Calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
print("Result:", a + b)
elif operator == "-":
print("Result:", a - b)
elif operator == "*":
print("Result:", a * b)
elif operator == "/":
if b != 0:
print("Result:", a / b)
else:
print("Cannot divide by zero")
else:
print("Invalid operator")
31. Complete Example — Student Result
marks = int(input("Enter marks: "))
if marks < 0 or marks > 100:
print("Invalid marks")
elif marks >= 90:
print("Grade: A")
elif marks >= 75:
print("Grade: B")
elif marks >= 60:
print("Grade: C")
elif marks >= 40:
print("Grade: D")
else:
print("Grade: F")
Example
Enter marks: 82
Grade: B
32. Quick Comparison
Statement Purpose
if Execute code when a condition is true
if-else Choose between two possibilities
Nested if Check a condition inside another condition
if-elif-e
lse
Choose between multiple possibilities
Ternary Short form of if-else
pass Empty placeholder for a block
33. Exam Questions to Practice
Basic
1. Write a Python program to check whether a number is positive or negative.
2. Write a program to check whether a number is even or odd.
3. Write a program to check voting eligibility.
4. Write a program to find the largest of two numbers.
5. Write a program to check whether a number is positive, negative, or zero.
Intermediate
6. Write a program to find the largest of three numbers.
7. Write a program to calculate student grades.
8. Write a program to check whether a year is a leap year.
9. Write a program to create a simple calculator using if-elif-else.
10. Write a program to calculate an electricity bill.
Nested if
11. Write a program to validate username and password.
12. Write a program to determine whether a student passed and, if so, whether they
received distinction.
13. Write a program to check whether a person is eligible for a loan based on age and
income.
Quick Revision
if
↓
Checks one condition
if-else
↓
Two possible choices
nested if
↓
if inside another if
if-elif-else
↓
Multiple choices
ternary
↓
Short form of if-else
Most Important Syntax
if condition:
statement
if condition:
statement
else:
statement
if condition1:
statement
elif condition2:
statement
else:
statement
if condition1:
if condition2:
statement
else:
statement
else:
statement
Remember: In Python, colon : + indentation are essential for conditional statements.