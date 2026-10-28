class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10**9 + 7
        n = max(instructions)
        tree = [0]*(n+2)

        def update(i):
            while i <= n:
                tree[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & -i
            return s

        ans = 0
        for i, val in enumerate(instructions):
            op1 = query(val - 1)
            op2 = i - query(val)
            ans += min(op1,op2)
            update(val)
            
        return ans % mod