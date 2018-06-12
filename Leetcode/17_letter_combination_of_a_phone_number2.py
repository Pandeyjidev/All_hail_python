class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        word_len = len(digits)
        letter_dict = {'2':['a','b','c'],
                       '3':['d','e','f'],
                       '4':['g','h','i'],
                       '5':['j','k','l'],
                       '6':['m','n','o'],
                       '7':['p','q','r','s'],
                       '8':['t','u','v'],
                       '9':['w','x','y','z']}
        res = [""]
        for c in digits:
            temp = []
            for d in letter_dict[c]:
                temp += [ec + d for ec in res]
            res = temp
        return res
        
            