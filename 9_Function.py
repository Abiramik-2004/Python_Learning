from math import *
a=10,20,30
print(type(a))
print(sqrt(10))
print(factorial(5))
print(pow(2,3))
print(sin(0))
print(ceil(4.2))
print(floor(4.2))
print(log(10))
print(log10(100)) #10?=100
print(pi)

#User defined function
def mul(b,c):
    print(b*c)
mul(10,2)
def add(b,c):
    print(b+c)
mul(0,0)
add(3,4)
add(20,4)

'''
There was four type of function
    ->With parameter without return type
    ->with parameter with return type
    -> without parameter without return type
    ->without parameter with return type

    a)With parameter without return type
        def func(msg):
            print(msg)
        func("hello")
    b) With parameter with return type
        def func(a):
            return a
        print(func(10))
    c) Without parameter without return type
        def func():
            print("Hello)
        func()
    d) Without parameter with return type
        def func():
            return "Hello"
        print(func())
        
'''
