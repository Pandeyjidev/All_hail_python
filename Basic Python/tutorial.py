li = [1,2,3]
other_li = [4,5,6]
li + other_li  # => [1, 2, 3, 4, 5, 6]
# Note: values for li and for other_li are not modified.

# Concatenate lists with "extend()"
li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]

# Remove first occurrence of a value
li.remove(2)  # li is now [1, 3, 4, 5, 6]
li.remove(2)  # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2)  # li is now [1, 2, 3, 4, 5, 6] again

# Get the index of the first item found
li.index(2)  # => 1
li.index(7)  # Raises a ValueError as 7 is not in the list

# Check for existence in a list with "in"
1 in li


################################################################################################################
#                                               DICTIONARY                                                     #
################################################################################################################


odr -> character to ASCII
chr -> ASCII to character

print (keyword.kwlist)

############################# LIST TO STRING #######################################################

By using ''.join

list1 = ['1', '2', '3']
str1 = ''.join(list1)
Or if the list is of integers, convert the elements before joining them.

list1 = [1, 2, 3]
str1 = ''.join(str(e) for e in list1)

################### create a null array ################
print(np.zeros((3,3)))
d = [0]*10



return [num for num in set(nums) if nums.count(num) > len(nums)/3]


from collections import Counter
class Solution:
    def frequencySort(self, s):
        return ''.join([ c*freq for c,freq in Counter(s).most_common()])