# heapq to realize priority queue
import heapq
import math
def delivery(allLocations, numDeliveries):
    minHeap = []
    results = []
    # Initialize heap
    heapq.heapify(minHeap)
    for i in range(len(allLocations)):
        if (allLocations[i]!= None):
            point = allLocations[i]
            heapq.heappush(minHeap,(math.sqrt(point[0]*point[0]+point[1]*point[1]), allLocations[i]))
    
    for i in range(numDeliveries):
        results.append(heapq.heappop(minHeap)[1])
    # results = heapq.nsmallest(numDeliveries, minHeap)


    return results

if __name__ == "__main__":
    list = [[1,2], [3,4], [1,-1]]
    num = 2
    print(delivery(list, num))

