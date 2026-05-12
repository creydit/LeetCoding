class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        for domains in cpdomains:
            x,y = domains.split(" ")
            arr = y.split('.')
            s = ''
            for d in arr[::-1]:
                s = d+'.'+s
                dic[s[:-1]] += int(x)
        ans = []
        for i,j in dic.items():
            x = str(j)+' '
            x += i
            ans.append(x)
        return ans