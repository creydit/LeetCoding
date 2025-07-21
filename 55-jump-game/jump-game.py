class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # TC - O(n) and SC- O(1)
        jump = 0
        for i in range(len(nums)):
            if i > jump:
                return False
            jump = max(jump, i + nums[i])
        return True