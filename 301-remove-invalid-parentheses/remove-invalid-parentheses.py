class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)

        def isValid(ss):
            cnt = 0
            for i in ss:
                if i=='(':
                    cnt += 1
                elif i==')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt==0
        
        q = deque()
        vis = {s}
        q.append(s)
        while q:
            ans = []
            for _ in range(len(q)):
                curr = q.popleft()
                if isValid(curr):
                    ans.append(curr)
                    continue
                for i in range(len(curr)):
                    if curr[i] not in "()": #to ignore letters
                        continue
                    sub = curr[:i]+curr[i+1:]
                    if sub not in vis:
                        q.append(sub)
                        vis.add(sub)
            if ans:
                return ans
        return []