l=int(input("Enter the starting no of range: "))
r=int(input("Enter the ending number of range: "))

max_fact=0
k=l
for i in range(l,r+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count>max_fact:
        max_fact=count
        k=i
print("Number: ",k)
print("no of factors : ",max_fact)
