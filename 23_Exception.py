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