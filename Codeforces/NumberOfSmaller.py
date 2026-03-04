'''
2 pointer
You are given two arrays, sorted in non-decreasing order. For each element of the second array, find the number of elements in the first array strictly less than it.

Input
The first line contains integers n
 and m
, the sizes of the arrays (1≤n,m≤105
). The second line contains n
 integers ai
, elements of the first array, the third line contains m
 integers bi
, elements of the second array (−109≤ai,bi≤109
).

Output
Print m
 numbers, the number of elements of the first array less than each of the elements of the second array.

Example
InputCopy
6 7
1 6 9 13 18 18
2 3 8 13 15 21 25
OutputCopy
1 1 2 3 4 6 6 


'''
n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
i = 0

c=[]
for j in range(m):
    while i < n and a[i] < b[j]:
            i += 1
    c.append(i)
            
 

print(*c)

