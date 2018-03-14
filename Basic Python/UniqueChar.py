from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1  
            
        for idx in range(len(s)):
            if dic[s[idx]] == 1:
                return idx

        return -1