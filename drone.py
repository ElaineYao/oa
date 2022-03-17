import heapq


def droneDelivery(maxTravelDist, forwardRouteList, returnRouteList):
    # maxheap - revert the number
    maxHeap = []
    heapq.heapify(maxHeap)
    flen = len(forwardRouteList)
    rlen = len(returnRouteList)
    # sort 2D list
    forwardRouteList = sorted(forwardRouteList, key=lambda i: i[1], reverse=True)  # Max ->min
    # print(forwardRouteList)
    returnRouteList = sorted(returnRouteList, key=lambda i: i[1])  # Min -?max
    # print(returnRouteList)
    for i in range(flen):
        for j in range(rlen):
            fpos = forwardRouteList[i]
            rpos = returnRouteList[j]
            sum = fpos[1] + rpos[1]
            if sum > maxTravelDist:
                break
            heapq.heappush(maxHeap, (-sum, [fpos[0], rpos[0]]))

    result = []
    max = 1
    #    print(maxHeap)
    for i in range(len(maxHeap)):
        pos = heapq.heappop(maxHeap)
        if pos[0] > max:
            break
        else:
            result.append(pos[1])
            max = pos[0]
    return result


if __name__ == "__main__":
    s1 = 10000
    l1 = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
    l2 = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
    print(droneDelivery(s1, l1, l2))
