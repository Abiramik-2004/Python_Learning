'''
    Consider a list of values from 10 to 15 and our target is 13. 
    i) write a linear search program
    ii)write binary search program

    
'''
#Linear Search
def linear_search(arr, tar):
    for i in range(len(arr)):
        if(arr[i]==tar):
            return i
    return -1
num=[10,11,12,13,14,15]
t=15
res=linear_search(num,t)
if res==-1:
    print("Not Found")
else:
    print("Found at ", res+1)

#BinarySearch
def Binary_Search(arr,t,l,h):
    if(l>h):
        return -1
    mid=(l+h)//2
    if(arr[mid]==t):
        return mid
    elif arr[mid]>t:
        return Binary_Search(arr,t,l,mid-1)
    else:
        return Binary_Search(arr,t,mid+1,h)

num=[10,11,12,13,14,15]
t=15
l=0
h=len(num)-1
res=Binary_Search(num,t,l,h)
if res==-1:
    print("Not Found")
else:
    print("Found at ", res+1)