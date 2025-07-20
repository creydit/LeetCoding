class Solution {
public:
    int numEnclaves(vector<vector<int>>& grid) {
        //BY multisource BFS from border 1's to check the connected reachable 1's and except all those 
        //count rest of the ones 
        //TC -O(4*N*M) and SC - O(N*M)
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<bool>> vis(n, vector<bool>(m, false));
        queue<pair<int,int>> q;
        for(int i = 0; i < n; i++){
            if(grid[i][0] == 1){
                vis[i][0] = true;
                q.push({i,0});
            }
            if(grid[i][m-1] == 1){
                vis[i][m-1] = true;
                q.push({i,m-1});
            }
        }
        for(int j = 0; j < m; j++){
            if(grid[0][j] == 1){
                vis[0][j] = true;
                q.push({0,j});
            }
            if(grid[n-1][j] == 1){
                vis[n-1][j] = true;
                q.push({n-1,j});
            }
        }
        int dx[] = {-1,0,1,0};
        int dy[] = {0,1,0,-1};
        while(!q.empty()){
            int r = q.front().first;
            int c = q.front().second;
            q.pop();
            for(int d = 0; d< 4; d++){
                int rr = r + dx[d];
                int cc = c + dy[d];

                if(rr>=0 && cc>=0 && rr<n && cc<m && !vis[rr][cc] && grid[rr][cc] == 1){
                    vis[rr][cc] = true;
                    q.push({rr,cc});
                }
            }
        }

        int ans = 0;
        for(int i = 0; i <n; i++){
            for(int j =0; j< m; j++){
                if(grid[i][j] == 1 && !vis[i][j]) ans++;
            }
        }
        return ans;
    }   
};