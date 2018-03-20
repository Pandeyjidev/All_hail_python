# https://www.leetfree.com/problems/palindrome-permutation.html#

def palindrom_perm(s):
    permutations = []
    s = list(s)
    for p in perm(s):
        permutations +=[p]
    # print(permutations)
    palin_perm = []
    for i in permutations:
        if is_palindrome(i) and (i not in palin_perm):
            palin_perm +=[i]
    print(palin_perm)

def is_palindrome(s):
    return s == s[::-1]

def perm(s):
    if len(s)==0:
        yield 0
    if len(s)==1:
        yield s
    else:
        for i in range(len(s)):
            x = s[i]
            xs = s[:i] + s[i+1:]
            for p in perm(xs):
                yield [x] + p

def permute_palin_brute(s):
    count = 0
    for i in range(128):
        c=0
        if(count > 1):
            break
        for i in range(len(s)):
            if ord(s[i]) == i:
                c +=1
        count +=c%2
    return count<=1

def permute_hashmap(s):
    count = {}
    for ss in s:
        if ss in count:
            count[ss] += 1
        else:
            count[ss] = 1 
    cnt = 0
    for c in count:
        if count[c]%2 == 1:
            cnt +=1
    return cnt<=1    

#  DOESN't Work
# def perm_set(s):
#     s_set = set(s)
#     return len(s)%len(s_set) <=1

# print(perm_set("aaabbccccxxsd"))


# print(permute_hashmap("abaab"))
# print(permute_palin_brute("abaab") )
# palindrom_perm("aab")