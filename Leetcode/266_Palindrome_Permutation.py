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


palindrom_perm("aab")