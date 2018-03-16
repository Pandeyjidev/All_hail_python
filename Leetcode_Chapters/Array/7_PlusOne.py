# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        carry = 0
        digits[0] +=1
        
        for i in range(len(digits)):
            digits[i] +=carry
            if digits[i]>=10:
                digits[i] -=10
                carry=1
            else:
                carry=0
                break
        if carry ==1:
            digits.append(1)
        digits.reverse()
        return digits