class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #Better by New Approach that doubling the string S to get every possible rotation of it as a substring!!
        #TC- O(n) SC-O(n)
        if len(s)!=len(goal):
             return False
        ds=s+s
        return ds.find(goal)!=-1


        #Brute force by checking all rotation to goal TC-O(n2) and SC-O(n)
        # if len(s)!=len(goal):
        #     return False
        # n=len(s)
        # for _ in range(n):
        #     s=s[1:]+s[0]
        #     if s==goal:
        #         return True
        # return False