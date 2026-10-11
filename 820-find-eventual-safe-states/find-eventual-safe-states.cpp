class Solution {
public:
    bool dfs(int node,vector<vector<int>> &adj, vector<int> &vis){
        if (vis[node]==1)return true;
        if (vis[node] == 2)return false;
        vis[node] = 1;
        for(auto nbr : adj[node]){
            if (dfs(nbr, adj, vis))return true;
        }
        vis[node] = 2;
        return false;
    }
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> vis(n,0);
        for(int i = 0; i < n; i++){
            if(vis[i] == 0){
                bool x = dfs(i,graph,vis);
            }
        }
        vector<int> ans;
        for (int i = 0; i < n; i++){
            if(vis[i] != 1)ans.push_back(i);
        }
        return ans;
    }
};