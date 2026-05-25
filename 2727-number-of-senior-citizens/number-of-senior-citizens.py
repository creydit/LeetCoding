class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for cust in details:
            age = int(cust[-4] + cust[-3])
            if age > 60:
                ans += 1
        return ans