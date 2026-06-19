class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #optimal
        #TC - O(N) and SC - O(1)
        curr = 0
        ans = curr
        for i in gain:
            curr += i
            ans = max(ans, curr)
        return ans

        #brute
        #TC - O(N+N) and SC - O(N+1)
        '''
        n = len(gain)
        ans = [0]
        for i in range(n):
            ans.append(ans[-1] + gain[i])
        return max(ans)
        '''
