# Method 1 
# use list comprehensions to go through one array and find other variables in the other
def intersection1(lst1,lst2):
    lst3 = [i for i in lst1 if i in lst2]
    return lst3

# Method 2
# using set()
def intersection2(lst1,lst2):
    return list(set(lst1)&set(lst2))

# Method 3
# using intersection() and set()
# Notice the capital I in the function name
def Intersection3(lst1,lst2):
    return set(lst1).intersection(lst2)

# Method 4
def intersection4(lst1,lst2):
    temp = set(lst1)
    lst3 = [ i for i in lst1 if i in lst2]
    return lst3
#Method5
# Python program to illustrate the intersection
# of two lists, sublists and use of filter()
def intersection5(lst1,lst2):
    #  look at it in 3 steps
    # step1 : for sublist in lst2
    # step2 : filter(lambda x:x in lst1, sublist)
    # step3 : [list(step2) step1]
    lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
    return lst3

lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]

print(intersection1(lst1, lst2))
print(intersection2(lst1, lst2))
print(Intersection3(lst1, lst2))
print(intersection4(lst1, lst2))

lst3 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
lst4 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
print(intersection5(lst3, lst4))
