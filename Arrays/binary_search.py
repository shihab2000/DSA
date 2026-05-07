def binarySearch(arr,targetval):
    left=0
    right=len(arr)-1
    while left <= right:
        mid =(left+right)//2

        if arr[mid]==targetval:
            return mid
        if arr[mid]<targetval:
            left=mid+1
        else:
            right=mid-1
    return -1

myArray=[1,2,3,4,5,6,7,8,9]
myTarget=11

result=binarySearch(myArray,myTarget)

if result != -1:
    print(f"Value {myTarget} found at index {result}")
else:
    print(f"value {myTarget} not found in array")