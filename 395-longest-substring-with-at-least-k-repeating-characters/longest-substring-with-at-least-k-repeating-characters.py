class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        def solve(left, right):
            if right - left < k:
                return 0
            
            freq = defaultdict(int)
            for i in range(left, right):
                freq[s[i]] += 1
            for i in range(left, right):
                if freq[s[i]] < k:
                    ll = solve(left,i)
                    rr = solve(i+1,right)
                    return max(ll,rr)
            return right - left

        return solve(0,n)