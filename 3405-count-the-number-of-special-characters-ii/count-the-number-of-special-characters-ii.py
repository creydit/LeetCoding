class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        #good solution 
        n = len(word)
        lastlow = defaultdict(int)
        firstup = defaultdict(int)
        for i in range(n):
            if word[i].islower():
                lastlow[word[i]] = i
            else:
                if word[i] not in firstup:
                    firstup[word[i]] = i
        ans = 0
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if i in lastlow and i.upper() in firstup and lastlow[i] < firstup[i.upper()]:
                ans += 1
        return ans


        #My Code T_T
        '''
        ans = 0
        dic = defaultdict(int)
        dic1 = defaultdict(int)
        for i in word:
            dic[i] += 1
    
        for i in word:
            dic1[i] += 1
            if i.isupper():
                x = i.lower()
                if dic1[x] == dic[x] and dic[x] > 0 and dic1[i] == 1:
                    ans += 1
                    dic[x] -= 1
        return ans
        '''