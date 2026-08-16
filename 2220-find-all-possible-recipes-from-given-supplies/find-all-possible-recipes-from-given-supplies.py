class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(len(recipes)):
            r = recipes[i]
            indegree[r] = len(ingredients[i])
            for ings in ingredients[i]:
                adj[ings].append(r)
        q = deque(supplies)
        ans = []
        while q:
            at = q.popleft()
            for res in adj[at]:
                indegree[res] -= 1
                if indegree[res] == 0:
                    ans.append(res)
                    q.append(res)
        return ans