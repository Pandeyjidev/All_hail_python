# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        
        res = ''
        
        for i in s:
            if (ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123) or (ord(i)>46 and ord(i)<58):
                res = res + i
        res = res.lower()
        print(res)
        print(res[::-1])
        return res[::-1] == res