class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def solve(idx, ss, temp):
            if idx >= n:
                return 
            if ss > target:
                return 
            if ss == target:
                ans.append(temp)
                return 
            solve(idx, ss+candidates[idx], temp+[candidates[idx]])
            solve(idx+1,ss,temp)

        solve(0,0,[])
        return ans