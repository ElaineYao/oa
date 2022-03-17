import heapq
def droneDelivery(maxTravelDist, forwardRouteList, returnRouteList):
   # maxheap - revert the number
   maxHeap = []
   heapq.heapify(maxHeap)
   flen = len(forwardRouteList)
   rlen = len(returnRouteList)
   # sort 2D list 
   sorted(forwardRouteList, key = lambda i:i[1], reverse=True) # Max ->min
   sorted(returnRouteList, key = lambda i:i[1]) # Min -?max
   for i in range(flen):
	   for j in range(r