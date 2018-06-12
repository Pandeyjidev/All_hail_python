def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if not nums: 
        return nums
    l = len(nums)
    i, j = l - 2, l - 1
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    while j > i and nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    nums[i+1:] = sorted(nums[i+1:])
    print(nums)
            

nextPermutation([3,2,1])