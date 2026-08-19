# Swapping by using a third variable
def swapNumTemp(a,b):
    print (f"a={a} and b={b} before Swapping")
    temp=a
    a=b
    b=temp
    print (f"a={a} and b={b} after Swapping")
swapNumTemp(20,10)

# Swapping by without using a third variables
def swapNum(a,b):
    print (f"a={a} and b={b} before Swapping")
    a = a+b
    b = a-b
    a = a-b
    print (f"a={a} and b={b} after Swapping")
swapNum(20,10)