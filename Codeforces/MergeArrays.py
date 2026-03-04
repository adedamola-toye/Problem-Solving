'''
A. Merging Arrays
time limit per test1 second
memory limit per test256 megabytes
For educational purposes, in the problems of this block, the time limit is large enough for the solution to pass in O(nlogn)
 time, but try to write the solution in linear time, which we discussed in the lecture.

You are given two arrays, sorted in non-decreasing order. Merge them into one sorted array.

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
Print n+m
 integers, the merged array.

Example
InputCopy
6 7
1 6 9 13 18 18
2 3 8 13 15 21 25
OutputCopy
1 2 3 6 8 9 13 13 15 18 18 21 25 

https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A
'''

n,m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i = 0
j = 0
output = []
while i < n and j < m:
    if arr1[i] < arr2[j]:
        output.append(arr1[i])
        i += 1
    else:
        output.append(arr2[j])
        j += 1
if i >= n and j < m:
    leftoversArr2 = arr2[j:m]
    output.extend(leftoversArr2)
if j >= m and i < n:
    leftoversArr1 = arr1[i:n]
    output.extend(leftoversArr1)

print(output)