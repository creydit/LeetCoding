class Solution:
    def frequencySort(self, s: str) -> str:
        # Naive Brute force with TC-O(n2 + nlogn + n) and SC-O(n)
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        x=dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
        ans=""
        for i,j in x.items():
            ans+=i*j
        return ans

