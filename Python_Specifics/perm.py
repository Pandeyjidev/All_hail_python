#Doesnt solve duplicate problems
def perm(lst):
    if len(lst) == 0:
        yield 0
    if len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm(xs):
                # print(p)
                yield [x]+p

def perm_without_yield(word):
    # print(word)
    if len(word) == 1:
        return [word]
    perms = perm_without_yield(word[1:])
    c = word[0]
    res = []
    for perm in perms:
        for i in range(len(perm)+1):
            res.append(perm[:i] + [c] + perm[i:])
    return res

data = list('abc')
# print(data)
for p in perm(data):
    print(p)
    pass

print(perm_without_yield(data))