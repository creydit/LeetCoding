class Solution {
public:
    /*
    int solve(int r, int c, vector<vector<int>> &grid,vector<vector<int>>& dp){
        if( r==0 && c==0 )return grid[r][c];
        if(r < 0 || c < 0) return 1e9;
        if(dp[r][c] != -1) return dp[r][c];
        int up = grid[r][c] + solve(r-1, c, grid, dp);
        int left = grid[r][c] + solve(r, c-1, grid, dp);

        return dp[r][c] = min(up,left);
    }
    */
    int minPathSum(vector<vector<int>>& grid) {
        //Tabulation 
        //TC - O(n*m) and SC - O(n*m)
        int n = grid.size();
        int m =grid[0].size();
        vector<vector<int>> dp(n, vector<int>(m, -1));
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(i==0 && j==0) dp[i][j] = grid[i][j];
                else{
                    int up = 0;
                    int left = 0;
                    up = grid[i][j] + (i > 0 ? dp[i-1][j] : 1e9);
                    left = grid[i][j] + (j > 0 ? dp[i][j-1] : 1e9);
                    dp[i][j] = min(up, left);
                }
            }
        }
        return dp[n-1][m-1];
        //Recursion + DP with memoization
        //TC - O(n*m) and SC - O(n+m+N*M)
        /*
        int n = grid.size();
        int m =grid[0].size();
        vector<vector<int>> dp(n, vector<int>(m, -1));
        return solve(n-1,m-1,grid,dp);
        */
    }
};