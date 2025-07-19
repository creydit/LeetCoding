class Solution {
public:
    void dfs(int at,  vector<vector<int>> aL, vector<bool> &vis){
        vis[at] = true;
        for(int j = 0; j < aL.size(); j++){
            if(aL[at][j] == 1){
                if(!vis[j]) dfs(j, aL, vis);
            }
        }
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        //TC - O(N + V + 2E) and SC - O( N + N) for vis arrays and recursion stack space 
        int n = isConnected.size();
        vector<bool> vis(n, false);

        //Simple algorithm to count the number of different DFS calls made thart will the num of provinces
        int ans = 0;
        for(int i = 0; i< n; i++){
            if(!vis[i]){
                ans++;
                dfs(i, isConnected, vis);
            }
        }
        return ans;
    }
};