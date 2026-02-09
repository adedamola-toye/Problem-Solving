'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freqDict = {}
        for n in nums:
            if n not in freqDict:
                freqDict[n] = 1
            else:
                freqDict[n] += 1
        
        freqValues = list(freqDict.values())
        freqValues.sort()
        maxFreq = freqValues[len(freqValues) - 1]

        for key,value in freqDict.items():
            if value == maxFreq:
                return key
    
        