class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        arr = []
        for i in range(n):
            arr.append((capital[i], profits[i]))
            
        arr = sorted(arr, key = lambda x: (x[0],-x[1]))

        idx = 0
        pq = []
        while k > 0:
            while idx < n and arr[idx][0] <= w:
                heapq.heappush(pq, -arr[idx][1])
                idx += 1
            if not pq:
                break
            w += (-1*heapq.heappop(pq))
            k -= 1
        return w