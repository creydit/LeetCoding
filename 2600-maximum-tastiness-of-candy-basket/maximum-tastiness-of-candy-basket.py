class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)
        lo = 0
        hi = 10**9
        while lo < hi:
            mid = (lo+hi+1)//2
            cnt = 1
            p = price[0]
            for i in range(1,n):
                if p + mid <= price[i]:
                    cnt += 1
                    p = price[i]
            if cnt >= k:
                lo = mid
            else:
                hi = mid - 1
        return lo