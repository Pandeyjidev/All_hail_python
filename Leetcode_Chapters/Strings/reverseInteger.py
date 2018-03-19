# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
#   Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output:  321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21



class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg =  False
        if x<0:
            neg = True
            x = -x
        value = int(str(x)[::-1])

        if value<2**31-1 or (value == 2**31 and neg):
            if neg:
                return - value
            else:
                return  value
        else:
            return 0