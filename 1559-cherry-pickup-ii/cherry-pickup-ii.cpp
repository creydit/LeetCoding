class Solution {
public:
    /*
    int solve(int i, int j1, int j2, int n, int m, vector<vector<int>>& grid, vector<vector<vector<int>>> &dp ){
        if( j1 < 0 || j1 >= m || j2 < 0 || j2 >= m) return -1e8;
        if ( i == n-1){
            if (j1==j2) return grid[i][j1];
            else return grid[i][j1] + grid[i][j2];
        }
        if( dp[i][j1][j2] != -1) return dp[i][j1][j2];
        int ans = -1e8;
        for(int dj1 = -1; dj1 <= 1; dj1++){
            for(int dj2 = -1; dj2 <= 1; dj2++){
                int value = 0;
                if(j1 == j2) value += grid[i][j1];
                else value += grid[i][j1] + grid[i][j2];
                value += solve(i+1, j1+dj1, j2+dj2, n, m, grid, dp);
                ans = max(ans, value);
            }
        }
        return dp[i][j1][j2] = ans;
    }
    */
    int cherryPickup(vector<vector<int>>& grid) {
        //Tabluation  
        // TC - O(n*m*m) and SC - O(n*m*m)
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>> (m, vector<int> (m, -1)));
        for(int j1 = 0; j1 <m; j1++){
            for(int j2 = 0; j2 < m; j2++){
                if(j1 == j2) dp[n-1][j1][j2] = grid[n-1][j1];
                else dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2];
            }
        }
        for(int i = n-2; i >= 0; i--){
            for(int j1 = 0; j1 < m; j1++){
                for(int j2 = 0; j2 < m; j2++){
                    int ans = -1e8;
                    for(int dj1 = -1; dj1 <= 1; dj1++){
                        for(int dj2 = -1; dj2 <= 1; dj2++){
                            int value = 0;
                            if(j1 == j2) value += grid[i][j1];
                            else value += grid[i][j1] + grid[i][j2];
                            if (j1+dj1 >= 0 && j1+dj1 < m && j2+dj2 >=0 && j2+dj2 < m)
                                value += dp[i+1][j1+dj1][j2+dj2];
                            else value += -1e8;
                            ans = max(ans, value);
                        }
                    }
                    dp[i][j1][j2] = ans;
                }
            }
        }
        return dp[0][0][m-1];
        //Recrusion + DP + memoization 
        //TC - O(n*m*m) and SC - O(n*m*m + n)
        /*
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>> (m, vector<int> (m, -1)));
        return solve(0, 0, m-1, n, m, grid, dp);
        */
    }
};