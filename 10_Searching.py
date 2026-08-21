'''Searching
--------------
It is the processes of seach an element from the collection 

Algorithm:

'''

numbers=[10,20,30,40,50,60]
target=60
for i in range(len(numbers)):
    if(numbers[1]==target):
        print("element is found at ", i)
        break
else:
    print("element is not found")


def linear_search(arr, tar):
    for i in range(len(arr)):
        if(arr[i]==tar):
            return i
    return -1
num=[1,2,3,4,5,6]
t=5
res=linear_search(num,t)
if res==-1:
    print("Not Found")
else:
    print("Found at ", res+1)



#Binary Search:
def binary_search(arr, tar, l, h):

    if l > h:
        return -1

    mid = (l + h) // 2

    if arr[mid] == tar:
        return mid

    elif arr[mid] > tar:
        return binary_search(arr, tar, l, mid - 1)

    else:
        return binary_search(arr, tar, mid + 1, h)


arr = [1, 2, 3, 4, 5, 6, 7]

l = 0
h = len(arr) - 1

target = 5

res = binary_search(arr, target, l, h)

if res == -1:
    print("Not Found")
else:
    print("Found at", res)

