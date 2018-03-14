# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
# Given an array of integers, find if the array contains any duplicates. 
# Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(len(nums)<=1):
            return False
        if(len(nums)==2):
            return nums[0]==nums[1]
        nums[:] = sorted(nums)
        print(nums)
        for i in range(1,len(nums)):
            if(nums[i]== nums[i-1]):
                return True
        return False