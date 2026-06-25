class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        #Brute force
        #using 2 loops and majority element concept 
        #TC - O(n2) and SC - O(1)
        n = len(nums)
        ans = 0
        for i in range(n):
            cnt = 0
            for j in range(i,n):
                if nums[j] == target:
                    cnt += 1
                else:
                    cnt -= 1
                if cnt>0:
                    ans += 1
        return ans 