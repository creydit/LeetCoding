class Solution {
    bool dfs(int at, int col, vector<vector<int>>& graph, vector<int> &color){
        color[at] = col;

        for(auto &next : graph[at] ){
            if(color[next] == -1){
                if( dfs(next, !col, graph, color) == false) return false;
            }
            else if(color[next] == col) return false;
        }
        return true;
    }
public:
    bool isBipartite(vector<vector<int>>& graph) {
        //DFS on graph and coloring the nodes with 2 colors
        //if we are successful on doning it then it is bipartite graph 
        //TC - O(V + 2E) and SC - O(V)
        int n = graph.size();
        vector<int> color(n, -1);

        for(int i = 0; i < n; i++){
            if(color[i]  == -1){
                if (dfs(i, 0, graph, color) == false) return false;
            }
        }
        return true;
    }
};