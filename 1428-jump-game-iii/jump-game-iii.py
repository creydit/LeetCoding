class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = [0] *(n+1)
        def solve(idx):
            if idx >= n or idx < 0:
                return False
            
            if arr[idx] == 0:
                return True
            
            if vis[idx] == 1:
                return False
                
            vis[idx] = 1
            left = idx + arr[idx]
            right = idx - arr[idx]
            ll = solve(left)
            rr = solve(right)
            return ll or rr

        return solve(start)
