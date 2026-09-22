try:
    num=int(input("Enter the num1:"))

except ValueError:
    print("Invalid Error")
else:
    print(num)
#--------------------------------------------------------
try:
    print(5/0)
except Exception as e:
    print("Expection occured")
finally:
    print("This block going to execute always...")

#-----------------------------------------------------------

age=int(input("Enter the age: "))
if age<18:
    try:
        raise ValueError("Age must be eighteen or more...")
    except:
        print("Please enter the age more than 18...")

else:
    print("eligibe")
#-----------------------
class insufficientBalanceError(Exception):
    pass
balance=int(input("Enter the balance amount: "))
withdrawl=int(input("Enter the amount you want to withdrawl: "))
if balance<withdrawl:
    try:
        raise insufficientBalanceError("Amount is insufficient")
    except:
        print("Please Enter the Sufficient amount to withdraw")
else:
    print("Amount is withdrawn...")

#----------------------------------------

'''Exception:
    Exception is an abnormal stop or sudden stop while occuring in a execution of a program.

Error vs Exeption
-----------------
            Error                 |   Exception
            -----                 | ----------
Often prevents code for executing | Occurs during execution
                                  |
May nees correction before running|  Can often be handled with try/Except
                                  |

Exception Handling Keywords:
----------------------------
    try-except-else, finally, and raise

Try:
----
    This block is responsible for exception occuring.

Except:
------
    The except block handles a particular exception.


'''
# MultipleExceptBlock
try:
    num=int(input("Enter the number: "))
    res=100/num
except ValueError:
    print("Please enter a valid number....")
except ZeroDivisionError:
    print("Number cannot be divided by zero")


# Multiple Exception in One except
try:
    num=int(input("Enter the Number: "))
    res=100/num
except (ValueError, ZeroDivisionError):
    print("Invalid input...")

'''
Else Block:
-----------
    The else block runs only when the try block completes without an exception.

'''

try:
    n=int(input("Enter the number: "))
    res=100/num
except ZeroDivisionError:
    print("Cannot divide by zero...")
else:
    print("Result: ",res)

'''
Finally Block:
-------------
    The finally block runs whether an exception ocuurs or not. 


'''
try:
    result=10/0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution completed")


#Getting Exeption information with as
try:
    res=10/0
except ZeroDivisionError as e:
    print("Error:",e)

'''
Common Built-in Exception:
--------------------------
✨ ZeroDivisionError=> Division by zero
✨ ValueError=>Correct type but ivalid value/form
✨ TypeError=>Incompatible data types
✨ IndexError=>Invalid Sequence index
✨ KeyError=>Missing dictionary key
✨ FileNotFoundError=> Requested file does not exist
'''
#-----------------------------------
'''
19. Complete try-except-else-finally Structure
try:
 # risky code
 pass
except ExceptionType as e:
 # error handling
 pass
else:
 # runs when no exception occurs
 pass
finally:
 # always runs
 pass
 
 '''
