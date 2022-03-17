import heapq
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        n = len(B)
        if n==1:
            return [A[0]+B[0]]
        A.sort(reverse=True)
        B.sort(reverse=True)
        maxb = B.pop(0)
        D = []
        for i in range(C):
            D.append(maxb+A[i])
        heapq.heapify(D)
        while n>1:
            maxb = B.pop(0)
            for ele in A:
                if maxb+ele < D[0]:
                    break
                else:
                    heapq.heappop(D)
                    heapq.heappush(D,maxb+ele)
            n-=1

        return sorted(D,reverse=True)
