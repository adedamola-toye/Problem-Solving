'''
The provided code stub reads an integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

0
1
4
Input Format

The first and only line contains the integer, .

Constraints


Output Format

Print  lines, one corresponding to each .

Sample Input 0

5
Sample Output 0

0
1
4
9
16
Language
Pypy 3
More
12345
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        square = i*i
        print(square)
Line: 5 Col: 22

Test against custom input
Congratulations!

You have passed the sample test cases. Click the submit button to run your code against all the test cases.


Sample Test case 0
Input (stdin)
5
Your Output (stdout)
0
1
4
9
16
Expected Output
0
1
4
9
16

'''


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        square = i*i
        print(square)