# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            x = target - num
            nums.remove(num)
            # print(nums)
            nums.insert(0,'x')
            try:
                if nums.index(x)>=0:
                    return [i,nums.index(x)]
            except:
                pass
            
            