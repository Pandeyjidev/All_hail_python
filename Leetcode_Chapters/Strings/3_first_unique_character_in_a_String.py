# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
# Given a string, find the first non-repeating character in it and return it's index. 
# If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        
        for l in s:
            if l in seen:
                seen[l] += 1
            else:
                seen[l] = 1
                
        for i, l in enumerate(s):
            if seen[l] == 1:
                return i
            
        return -1