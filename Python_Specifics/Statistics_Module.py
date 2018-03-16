import statistics 

example = [1,2,312,245,23,12,234,1]

m = statistics.mean(example)
sd = statistics.stdev(example)
med = statistics.median(example)
mode = statistics.mode(example)
var = statistics.variance(example)

print(m)
print(sd)
print(med)
print(mode)
print(var)