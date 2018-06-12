import bisect
def kEmptySlots(flowers, k):
    blooming = []
    for day, flower in enumerate(flowers, 1):
        i = bisect.bisect(blooming, flower)
        for neighbor in blooming[i-(i>0):i+1]:
            if abs(flower - neighbor) - 1 == k:
                return day
        blooming.insert(i, flower)
    return -1

arr = [1,3,2]
k = 1
print(kEmptySlots(arr,k))