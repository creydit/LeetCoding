class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        #Brute force
        #TC - O(N + N + (Max - Min)* logN ) and SC - O(N)
        start = min(nums)
        end = max(nums)
        st = set(nums)
        ans = []
        for i in range(start+1, end):
            if i not in st:
                ans.append(i)
        return ans