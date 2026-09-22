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