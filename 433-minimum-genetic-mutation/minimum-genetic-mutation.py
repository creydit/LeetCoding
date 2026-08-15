class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        options = ['A','C','G','T']
        vis = set()
        q = deque()
        q.append((startGene,0))
        vis.add(startGene)
        ans = -1
        while q:
            gene,lvl = q.popleft()
            if gene == endGene:
                ans = lvl
                break
            for i in range(8):
                for ops in options:
                    newGene = gene[:i]
                    if ops != gene[i]:
                        newGene += ops
                        newGene += gene[i+1:]
                        if newGene in bank and newGene not in vis:
                            vis.add(newGene)
                            q.append((newGene,lvl+1))
        return ans