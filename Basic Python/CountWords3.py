from collections import Counter
# from collections import elements
import re
# Read using Counter
data_list = ["word1","word1","word1","word3","word3","word1","word2","word2","word1","word1","word2"]
cnt = Counter()
for word in data_list:
    cnt[word] +=1
print(cnt)

# Read using RegEx
word = re.findall('\w+', open('text.txt').read().lower())
print(word)
# print(list(word.elements()))


# most_common([n])
# Return a list of the n most common elements and their counts from the most common to the least. 
# If n is not specified, most_common() returns all elements in the counter. 
# Elements with equal counts are ordered arbitrarily:
print(Counter('abracadabra').most_common(3))
# [('a', 5), ('r', 2), ('b', 2)]