class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        #Brute force
        #TC - O(N) and SC - O(N)
        n = len(arr)
        dic = {}
        nums = sorted(arr)
        rank = 1
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = rank
                rank += 1
        for i in range(n):
            arr[i] = dic[arr[i]]
        return arr