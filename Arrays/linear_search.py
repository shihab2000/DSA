def linearSearch(arr,targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

arr=[4,2,6,3,9,1,7]
targetval=9

result=linearSearch(arr,targetval)

if result != -1:
    print(f"Value {targetval} found at index {result}")
else:
    print(f"Value {targetval} not found ")
