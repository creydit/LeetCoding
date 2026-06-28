class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        #by sorting and checking since there is no condition on number of ops
        #TC - O(nlogn) and SC - O(1)
        arr.sort()
        n = len(arr)
        if arr[0] != 1:
            arr[0] = 1
        ans = arr[0]
        for i in range(1,n):
            if arr[i] - 1 > arr[i-1]:
                arr[i] = arr[i-1] + 1
            ans = max(ans, arr[i])
        return ans