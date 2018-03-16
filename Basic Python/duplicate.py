def has_duplicate(arr):
    a=set(arr)
    return len(arr)==len(a)


print(has_duplicate([1,2,3,4,5,6,7,8,9]))
print(has_duplicate([1,1,2,3,4,5,6,7,8]))
print(has_duplicate([1,'.',2,'.',1,6,7,8,9]))