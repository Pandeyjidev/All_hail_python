# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
# Given an array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:]=sorted(nums)
        for i in range(1,len(nums),2):
            if(nums[i]!=nums[i-1]):
                return nums[i-1]
        return nums[-1]