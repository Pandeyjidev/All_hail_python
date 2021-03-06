# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
# Given two strings s and t, write a function to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

# Note:
# You may assume the string contains only lowercase alphabets.

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = ''.join(sorted(s))
        tt = ''.join(sorted(t))
        return ss==tt