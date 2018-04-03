def permute_iteration(nums):
    l = len(nums)
    res = []
    temp = []
    for n in nums:
        temp.append([n])
        # print(temp)
    while(temp):
        q = temp.pop()
        
        if len(q) > l:
            break
        elif len(q) == l:
            res.append(q)
        # print(q)
        # print(nums)
        for n in nums:
            if not n in q:
                temp.append(q + [n])
                # print(temp)
                # print("\n")
    return res
def permute_recursive(nums):
    m= len(nums)
    res = []
    def pp(x):
        if len(x) == m:
            res.append(x)
            return []
        else:
            r = []
            for n in nums:
                if not n in x:
                    r += x + [n] + pp(x + [n])
            return r
    pp([])
    return res
a = [1,2,5]
# print(permute_iteration(a))
print(permute_recursive(a))