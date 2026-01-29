'''Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution(object):
    def isPalindrome(self, x):
        """`
        :type x: int
        :rtype: bool
        """
        stringX = str(x)
        normalList = []
        reversedList = []
        for i in range(0,len(stringX)):
            normalList.append(stringX[i])
        print(normalList)
        for i in range(len(stringX)-1,-1,-1):
            reversedList.append(stringX[i])
        print(reversedList)
        if normalList == reversedList:
            return True
        else:
            return False

 
'''First Approach
Convert the integer to string - so that we can account for cases like negativve numbers.
If there were no extra characters like -, we could have just addressed it as an integer.
Then, loop through the string in a forward direction and create a list (a normal list)
Loop through the string in a reverse direction and create a reversed list.
Compare these 2 lists together. If they are the same then its a palindrome number
-121 ->normal - ['-', '1', '2', '1'] 
reversed - ['1', '2', '1', '-']

Time complexity - 4O(n) 
converting input to string - n times
loop1 - runs n times for normalList building
loop2 - runs n times for reversed list building
comparing 2 lists - O(n)
Total = 4O(n)

Space complexity - O(n)
creating a new string when converting input to string
creating 2 separate lists 
each of these takes O(n) space
'''       



class Solution(object):
    def isPalindrome(self, x):
        """`
        :type x: int
        :rtype: bool
        """
        stringX = str(x)
        return bool(stringX == stringX[::-1])
    
'''
Time complexity - O(n)
str(x) is O(n)
Then stringX[::-1] is a single slice operation. Even though it's one line, Python still has to visit every character to copy it, so it's O(n).

Space : O(n)
'''

        
