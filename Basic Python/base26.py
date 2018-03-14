class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        base = ord('Z')-ord('A')+1
        
        while n > 0:
            curr = n % base
            
            if curr == 0: 
                res += 'Z'
                n = int(n/base)-1
            else:
                res += chr(curr + ord('A') - 1)
                n = int(n/base)
            
            
        return ''.join(reversed(res))