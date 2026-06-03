class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        L = 0
        LC = 0
        LCT = 0
        prefL =[0]*(n+1)
        prefLC=[0]*(n+1)
        for i in range(n):
            prefL[i] = L
            prefLC[i] = LC
            if s[i] == 'L':
                L+=1
            elif s[i] == 'C':
                LC += L
            elif s[i] == 'T':
                LCT += LC
        prefL[n] = L
        prefLC[n] = LC
        T = 0
        CT = 0
        suffT = [0]*(n+1)
        suffCT = [0]*(n+1)
        for i in range(n-1,-1,-1):
            if s[i] == 'T':
                T += 1
            elif s[i] == 'C':
                CT += T
            suffT[i] = T
            suffCT[i] = CT
        suffT[n] = 0
        suffCT[n] = 0
        gl=0
        gc=0
        gt=0 
        for i in range(n+1):
            gl = max(gl,suffCT[i])
            gc = max(gc, prefL[i]*suffT[i])
            gt = max(gt, prefLC[i])
        ans = LCT + max(gl,gc,gt)
        return ans
        
            
            

