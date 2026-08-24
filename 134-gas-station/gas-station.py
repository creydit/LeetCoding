class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #TC - O(n) and SC - O(1)
        n = len(gas)
        buffer = 0
        start = 0
        buffer2 = 0
        for i in range(n):
            buffer += gas[i] - cost[i]
            buffer2 += gas[i] - cost[i]
            if buffer2 < 0:
                buffer2 = 0
                start = i+1
        if buffer < 0:
            return -1
        return start

        #TC - O(n^2) and SC- O(N)
        '''
        n = len(gas)
        possibleStartIndex = []
        for i in range(n):
            if gas[i] >= cost[i]:
                possibleStartIndex.append(i)
        ans = -1
        idx = 0
        while idx < len(possibleStartIndex):
            start = possibleStartIndex[idx]
            k = 0
            buffer = 0
            while k < n:
                buffer += gas[start] - cost[start]
                if buffer < 0:
                    break
                start +=1
                start %= n
                k += 1
            if k==n:
                ans = possibleStartIndex[idx]
                break
            idx += 1
        return ans
        '''
