t=(10,20,30,40,50)
print(t[-1])


'''
   Tuples:
        A tuple is Ordered, immutable in nature
        It allows duplicates
        It is used to store the unique values 
        Can contains different datatypes
        used parentheses to create the tuple

    Single element tuples:
    t1=(1,)

    Indexing:
    number=(10,20,30)
    number[1]=20
    // Negative indexing
    number[-1]=30
    number[-2]=20
    number[-3]=10

    Slicing:
    num[start:stop:step]

    Methods:
    count()--return how many time the value occurs
    index()--return the index of the first occurence

    Joining tuples:
    + Operator used to createa new tuple

    Repeating in tuple:
    * Operator is used to reated a tuple

    Membership operator:
    in
    nt in

    Reversing a tuple
    tuple[::-1]



'''
t=(1,2)
print(t+t)
print(t*5)

print(1 in t)
print(5 not in t)
print(5 in t)

