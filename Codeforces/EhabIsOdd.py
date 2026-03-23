n = int(input())
arr = list(map(int, input().split()))


def hasEven(arr):
    for n in arr:
        if n%2 == 0:
            return True
    return False
    
def hasOdd(arr):
    for n in arr:
        if n%2 != 0:
            return True
    return False
    
if hasEven(arr) and hasOdd(arr):
    print(sorted(arr))
else:
    print(*(arr))
    