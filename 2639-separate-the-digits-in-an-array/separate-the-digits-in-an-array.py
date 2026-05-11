class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums[::-1]:
            x = i
            while x>0:
                answer.append(x%10)
                x//=10
        return answer[::-1]
        
        '''
        answer = []
        for i in nums:
            x = str(i)
            for j in x:
                answer.append(int(j))
        return answer
        '''