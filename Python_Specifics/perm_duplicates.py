#  https://codereview.stackexchange.com/questions/132704/counting-permutations-without-repetitions-for-a-number-or-a-string
# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

import itertools
from timeit import timeit
def permute_itertools_and_set(word):
    return( set([''.join(i) for i in itertools.permutations(word)]))

def permutations(L):
    if len(L) == 1:
        yield [L[0]]
    elif len(L) >= 2:
        (a, b) = (L[0:1], L[1:])
        for p in permutations(b):
            for i in range(len(p)+1):
                yield b[:i] + a + b[i:]
def permute_with_duplicates(word):
    if len(word) == 0:
        yield 0
    if len(word)  == 1:
        yield [word]
    else:
        for i in range(len(word)):
            for p in permute_with_duplicates(word[:i]+word[i+1:]):
                yield [word[i]] + p

                
data = "AACB"
# for i in permutations(data):
#     print(i)

lst = []

for i in permute_with_duplicates(data):
    lst.append(i)
print(len(lst))