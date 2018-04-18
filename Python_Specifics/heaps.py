import heapq


if __name__ == '__main__':
    h = [1,9,3,8,5,6,23,12,0]
    heapq.heapify(h)
    print("Heap : ",h)
    heapq.heappush(h,(1,'food'))
    heapq.heappop(h)
    print("Heap : ",h)