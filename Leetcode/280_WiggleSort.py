# Sort and Swap the second elements
def wiggleSort(lst):
    lst.sort()
    for i in range(1,len(lst)-1,2):
        lst[i+1],lst[i] = lst[i],lst[i+1]
    # print(lst)
    return lst

# Sort each  by checking conditions
def wiggleSort2(lst):
    for i in range(len(lst)-1):
        if((i%2==0 and lst[i]>lst[i+1]) or (i%2==1 and lst[i]<lst[i+1])):
            lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst

nums = [3,5,2,1,6,4]
print(wiggleSort(nums))
print(wiggleSort2(nums))