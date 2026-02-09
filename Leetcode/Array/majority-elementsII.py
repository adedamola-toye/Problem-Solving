'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freqDict = {}
        for n in nums:
            if n not in freqDict:
                freqDict[n] = 1
            else:
                freqDict[n] += 1
        
        freqVals = freqDict.values()
        output =[]
        for key, value in freqDict.items():
            if value > (len(nums) // 3):
                output.append(key)
        return output