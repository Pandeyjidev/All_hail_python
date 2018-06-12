class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # [2,2,2,2,3,4,5]
        # 4
        sum_num = sum(nums)
        target,rem = divmod(sum_num,k)
        if rem>0 or k>sum_num:
            return False
        visited = [False for _ in range(len(nums))]
        def dfs(k,target,currsum, curr_idx):
            if k==1 and currsum == target:
                return True
            if currsum == target:
                return dfs(k-1,target,0,0)
            else:
                for idx in range(curr_idx,len(nums)):
                    if currsum+nums[idx] <= target and not visited[idx] :
                        visited[idx] = True
                        if dfs(k,target,currsum+nums[idx],idx+1):
                            return True
                        visited[idx] = False
            return False
        return dfs(k,target,0,0)






# Best Solution in Leetcode
# https://leetcode.com/submissions/detail/154525273/

# class Solution(object):
#     def canPartitionKSubsets(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         if sum(nums) % k != 0: return False
        
#         target = sum(nums) / k
        
#         nums.sort(reverse = True)
#         if nums[0] > target: return False
        
#         removed = [False] * len(nums)
        
#         def findTarget(index, target):
#             if target == 0: return True
#             if index == len(nums): return False
#             for i in xrange(index, len(nums)):
#                 if removed[i] or nums[i] > target: continue
#                 if nums[i] == target:
#                     removed[i] = True
#                     return True
#                 if findTarget(i + 1, target - nums[i]):
#                     removed[i] = True
#                     return True
#             return False
        
#         for i in xrange(len(nums)):
#             if not removed[i]:
#                 if not findTarget(i, target):
#                     return False
#         return True