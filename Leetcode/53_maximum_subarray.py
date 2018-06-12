class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max_rsum, max_so_far = nums[0],nums[0]
        
        for i in range(1, len(nums)):
            cur_max_rsum = max(nums[i], cur_max_rsum + nums[i])
            max_so_far = max(max_so_far, cur_max_rsum)
        
        return max_so_far