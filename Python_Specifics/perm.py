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



data = list('abc')
# print(data)
for p in perm(data):
    print(p)