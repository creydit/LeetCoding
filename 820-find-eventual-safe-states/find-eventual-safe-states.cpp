class Solution {
    bool dfs(int at, vector<bool> &vis, vector<bool> &pathVis, vector<vector<int>> &graph, vector<bool> &safeNode){
        vis[at] = true;
        pathVis[at] = true;

        for(auto next : graph[at]){
            if(!vis[next]){
                if (dfs(next, vis, pathVis, graph, safeNode)) return true;
            }
            else if(pathVis[next]){
                return true;
            }
        }
        safeNode[at] = true;
        pathVis[at] = false;
        return false;
    }
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        //BY DFS detecting cycle and all those nodes connected to cycle will not be safe nodes
        int n = graph.size();
        vector<bool> vis(n, false);
        vector<bool> pathVis(n,false);
        vector<bool> safeNode(n, false);

        for(int i = 0; i < n; i++){
            if(!vis[i]){
                dfs(i, vis, pathVis, graph, safeNode);
            }
        }
        vector<int> ans;
        for(int i = 0; i <n; i++){
            if(safeNode[i]) ans.push_back(i);
        }
        return ans;
    }
};