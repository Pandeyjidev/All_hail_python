class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for idx in range(len(digits)-1,-1,-1):
            if digits[idx]+carry<10:
                digits[idx] += carry
                carry = 0
                break
            else:
                digits[idx] = 0
        if carry == 0:                
            return digits
        
        digits.insert(0,1)
        return digits