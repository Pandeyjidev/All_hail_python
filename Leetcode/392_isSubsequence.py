class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        s_runner = t_runner = 0
        while s_runner<len(s) and t_runner<len(t):
            if s[s_runner] == t[t_runner]:
                s_runner +=1
                t_runner +=1
            else:
                t_runner +=1
        print(s_runner)
        return True if s_runner == len(s) else False