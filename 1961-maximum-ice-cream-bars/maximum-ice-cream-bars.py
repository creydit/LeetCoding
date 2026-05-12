class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        #Counting Sort 
        mx = max(costs)
        freq = [0]*(mx+1)
        for i in costs:
            freq[i] += 1
        ans = 0
        for i in range(1,mx+1):
            if freq[i] > 0:
                take = coins//i
                if freq[i] <= take:
                    ans += freq[i]
                    coins -= (freq[i]*i)
                else:
                    ans += take
                    coins -= (take*i)
        return ans
                
        #Normal way
        '''
        n = len(costs)
        costs.sort()
        ans = 0
        for i in range(n):
            if coins >= costs[i]:
                ans += 1
                coins -= costs[i]
            else:
                break
        return ans
        '''