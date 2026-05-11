class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            x = str(i)
            for j in x:
                answer.append(int(j))
        return answer