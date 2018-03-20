def isSortedArray(lst,idx):
    if len(lst)==1:
        return 1
    if(lst[idx-1]<=lst[idx-2]):
        return 0
    else:
        return isSortedArray(lst,idx-1)

nums = [1,22,3,4,5,36,7]
print(isSortedArray(nums,len(nums)-1))
nums.sort()
print(type(nums))
print(isSortedArray(nums,len(nums)-1))