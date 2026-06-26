class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        #Magical O(n) solution using dictionary to store the already seen prefix sums and 
        #checking how many pref[l-1] < pref[r] and conunting it all.
        #TC - O(n) and SC - O(n)
        n = len(nums)
        pref = 0
        dic = defaultdict(int)
        dic[pref] += 1
        ans = 0
        validStarts = 0
        for i in range(n):
            if nums[i] == target:
                validStarts += dic[pref]
                pref += 1
            else:
                pref -= 1
                validStarts -= dic[pref]
            ans += validStarts
            dic[pref] += 1

        return ans 
