num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
print("choose operator: \n1.Addition\n2.Subraction\n3.Multiplication\n4.Division" \
"")
op=int(input("Enter the option: "))
if op==1:
    print(num1+num2)
elif op==2:
    print(num1-num2)
elif op==3:
    print(num1*num2)
elif op==4:
    if(num2==0):
        print("Cannot divisible by 0")
    else:
        print(num1/num2)
else:
    print("invalid operator")



