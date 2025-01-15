class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        Sn = (n * (n + 1)) // 2
        S2n = (n * (n + 1) * (2 * n + 1)) // 6
        Tn = 0
        T2n = 0

        for num in nums:
            Tn += num
            T2n += num * num

        xy = Sn - Tn
        x2y2 = S2n - T2n
        xpy = x2y2 // xy

        x = (xy + xpy) // 2
        y = x - xy

        return [y, x]