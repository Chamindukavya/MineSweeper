import math
def solve(arr):
    # Write your code here
    n = len(arr)
    arr.sort()
    
    newSet = set(arr)
    print(newSet)
    newArr = list(newSet)
    newArr.sort()
    count = len(newArr)-1

    print(math.factorial(count))

solve([1,1,2,4,2])