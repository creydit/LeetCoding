class Solution:
    def minimumLength(self, s: str) -> int:
        freq=Counter(s)
        ans=0
        for y in freq.values():
            if y%2==0:
                ans+=2
            else:
                ans+=1
        return ans 