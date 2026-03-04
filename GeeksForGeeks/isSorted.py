TWO POINTER

'''
Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.
Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted.
Constraints:
1 ≤ arr.size ≤ 106
- 109 ≤ arr[i] ≤ 109
'''

class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        isSorted = True
        i = 0
        j = 1
        while i < j and  j < len(arr):
            if arr[i] > arr[j]:
                isSorted = False
            i += 1
            j += 1
        
        return isSorted