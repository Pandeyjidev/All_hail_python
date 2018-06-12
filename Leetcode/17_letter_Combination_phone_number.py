class Solution(object):
    def letterComb(self, digits, Map):
        if len(digits) == 1:
            try:
                for s in Map[digits]:
                    yield s
            except:
                return []
        else:
            for s in Map[digits[0]]:
                for ss in self.letterComb(digits[1:], Map):
                    yield s + ss
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return []
        Map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result = []
        for ss in self.letterComb(digits, Map):
            result.append(ss)
        return result