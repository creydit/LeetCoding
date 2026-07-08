class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        #Optimal using prefix computations
        #TC - O(Q+N) and SC - O(3N)
        mod = 1000000007

        n = len(s)

        pref = [0]*(n)
        pref[0] = int(s[0])
        for i in range(1,n):
            pref[i] = pref[i-1]+int(s[i])

        nums = [0]*n
        nums[0] = int(s[0])
        pow10 = [0]*n
        pow10[0] = 1
        for i in range(1,n):
            if s[i] == '0':
                nums[i] = nums[i-1]
                pow10[i] = pow10[i-1]
                continue
            nums[i] = (nums[i-1]*10 + int(s[i])) % mod
            pow10[i] = pow10[i-1]+1

        pow10mod = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10mod[i] = (pow10mod[i-1] * 10) % mod

        ans = []
        for l,r in queries:
            if l==0:
                ss = pref[r]
                n1 = nums[r]
                n2 = 0
                exp = pow10[r]
            else:
                ss = pref[r]-pref[l-1]
                n1 = nums[r]
                n2 = nums[l-1]
                exp = pow10[r]-pow10[l-1]
            number = n1- n2*pow10mod[exp]
            ans.append((ss*number)%mod)
            
        return ans 

        #Brute force 
        '''
        def solve(s):
            ss = 0
            n = 0
            for i in s:
                ss += int(i)
                if i!='0':
                    n *=10
                    n += (int(i))
            return ((ss*n)%mod)
        ans = []
        for l,r in queries:
            ans.append(solve(s[l:r+1]))
        return ans
        '''