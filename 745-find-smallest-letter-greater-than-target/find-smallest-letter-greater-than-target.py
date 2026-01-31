class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        for i in range(n):
            if i==0:
                if letters[i] > target:
                    return letters[i]
                if letters[i]==letters[i+1]:
                    continue
                if letters[i] == target:
                    continue
            if letters[i] > target:
                return letters[i]
            if letters[i] == letters[i-1]:
                continue
            if letters[i] == target:
                continue
            
        return letters[0]