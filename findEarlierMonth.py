import math

def findEarliestMonth(stockPrice):
    left = 0
    right = sum(stockPrice)
    n = len(stockPrice)
    net = float('inf')
    idx = -1
    for i in range(1, n):
        left += stockPrice[i-1]
        right -= stockPrice[i-1]
        temp = abs(math.floor(left/i) - math.floor(left/(n-i)))
        if (temp < net):
            net = temp
            idx = i
    return idx

if __name__ == "__main__":
    s = [1, 3, 2, 3]
    print(findEarliestMonth(s))

