class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        vis = [0]*n
        q = deque()
        q.append(0)
        vis[0] = 1
        far = 0
        while q:
            at = q.popleft()
            if at == n-1:
                return True
            start = max(far,at + minJump)
            end = min(at+maxJump, n-1)
            for i in range(start, end+1):
                if vis[i] == 0 and s[i] == '0':
                    q.append(i)
                    vis[i] = 1
            far = end + 1
        return False
