class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''
        for i in board:
            for j in i:
                start += str(j)

        adj = [[1,3], [0,2,4], [1,5], [0,4], [1,3,5], [2,4]]

        target = "123450"

        q = deque()
        q.append((start,0))
        vis = {start}
        ans = -1
        while q:
            at,moves = q.popleft()

            if at == target:
                ans = moves
                break

            idx = at.find('0')

            for neigh in adj[idx]:
                arr = list(at)
                arr[neigh], arr[idx] = arr[idx], arr[neigh]
                new = ''.join(arr)
                if new not in vis:
                    vis.add(new)
                    q.append((new,moves+1))
        return ans
        
            