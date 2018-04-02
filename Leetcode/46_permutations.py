class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permutations(num):
            if len(num) ==0:
                yield 0
            if len(num) == 1:
                yield num
            else:
                for i in range(len(num)):
                    x = num[i]
                    xs = num[:i] + num[i+1:]
                    for j in permutations(xs):
                        yield [x] + j
            
        lst = []
        for p in permutations(nums):
            lst.append(p)
        print(lst)
        return lst
        
        
        