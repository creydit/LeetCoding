class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Worst case - O(n) thats why it better to use min (linear search)
        return min(nums)