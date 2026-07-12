class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n==0:
            return []
        nums = []
        for i in range(n):
            nums.append((arr[i],i))
        nums.sort()
        idx = nums[0][1]
        arr[idx] = 1
        rank = 1
        for i in range(1,n):
            if nums[i][0] == nums[i-1][0]:
                idx = nums[i][1]
                arr[idx] = rank
            else:
                rank += 1
                idx = nums[i][1]
                arr[idx] = rank 
        return arr

        #Brute force
        #TC - O(NlogN) and SC - O(N)
        '''
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
        '''