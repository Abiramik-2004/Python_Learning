'''
SET:
    set is an unordered collection of datas. It is mutable in nature.
    It doesn't follow the indexed value acess

    Adding element
    --add()
    --update() 

    Removing element
    --remove()
    --pop()
    --discard()
    --clear()

SET OPERATION:

    Union:
        It combines all elemnts 
        -- | or union()
    
    Intersection:
        Returns Common elements
        -- & or intersection()

    Differences:
        Return element which is not present in a set2 from set 1
    
    Symmetric Differences:
        Return elemets non common from both the set 

    Subset & Superset
    -----------------
    Subset:
        Set A is a subset B means If every elements of A is also present in B
        A.issubset(B)
    Superset:
        Set B is a superset of A means if B contains all the element present in A
        B.issuperset(A)
    DisJoinSet
    -----------
        Two sets are disjoint if they have no common elements
        A.isdisjoint(B)
    Frozenset
    ---------
        A frozenset is an immutable set
        Once created, you cannot add, remove, or change elements
        frozenset({1,2,3})
'''
num={10,20,30,40,50}
print(type(num))
print(num)

# creation of empty set
n=set()
print(type(n))

num={70,10,20,60,60}
print(num)


num={1,2,3,5}
num.add(4)
print(num)
num.update([6,7,8,9,10])
print(num)
num.remove(2)
print(num)

num.discard(20)
num.discard(1)
print(num)

x=num.pop()
print(x)

num.clear()
print(num)
print(len(num))

#union
s1={"a","b","c"}
s2={"c","d","e","f"}
result=s1|s2
print(result)

#Intersection
result=s1&s2
print(result)

#difference
result=s1-s2
print(result)

#Symmetric difference
result=s1^s2
print(result)


#DisJoint
print(s1.isdisjoint(s2))

#FrozenSet
num=frozenset({1,2,3})

#Subset & Superset
A={1,2,3}
B={1,2,3,4,5}
print(A.issubset(B))
print(B.issuperset(A))

