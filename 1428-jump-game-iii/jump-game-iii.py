class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        #BFS 
        n = len(arr)
        vis = [0]*(n+1)
        q = deque()
        q.append(start)
        vis[start] = 1
        while q:
            at = q.popleft()

            if arr[at] == 0:
                return True

            left = at - arr[at]
            right = at + arr[at]

            if left >= 0 and vis[left] == 0:
                vis[left] = 1
                q.append(left)
            if right < n and vis[right] == 0:
                vis[right] = 1
                q.append(right)
        return False


        #DFS
        '''
        n = len(arr)
        vis = [0] *(n+1)
        def solve(idx):
            if idx >= n or idx < 0 or vis[idx]:
                return False
            
            if arr[idx] == 0:
                return True

            vis[idx] = 1
            left = idx + arr[idx]
            right = idx - arr[idx]
            ll = solve(left)
            rr = solve(right)
            return ll or rr

        return solve(start)
        '''
