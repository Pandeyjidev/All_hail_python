def diffWaysToCompute(input):
    print(input)
    res = []
    for i, char in enumerate(input):
        if char in "+-*":
            print("Calling Left")
            part1 = diffWaysToCompute(input[:i])
            print("Calling Right")
            part2 = diffWaysToCompute(input[i + 1:])
            print("Compute {} and {}".format(part1,part2))
            for x in part1:
                res += [eval(str(x) + char + str(y)) for y in part2]
                print(res)
    if len(res) == 0:
        res.append(eval(input))
    return res

print(diffWaysToCompute("2*3-1+11-1"))