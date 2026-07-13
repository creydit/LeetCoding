class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        #TC - O(nlogn, n is max num of increasing digits) and SC - O(1)
        ans = []
        s = '123456789'
        l = 0
        for l in range(9):
            numS = ''
            for r in range(l,9):
                numS+=s[r]
                num = int(numS)
                if low<=num<=high:
                    ans.append(num)
        ans.sort()
        return ans
