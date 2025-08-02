class Solution {
public:
    /*
    int solve(int r, int c, vector<vector<int>>& dp){
        if(r == 0 && c == 0) return 1;
        if(r < 0 or c < 0) return 0;

        if(dp[r][c] != -1 ) return dp[r][c];

        int up = solve(r-1, c, dp);
        int left = solve(r, c-1, dp);
         
        return dp[r][c] = up+left;
    }
    */
    int uniquePaths(int m, int n) {
        //Space Optimised DP
        // TC - O(n*m) and SC - O(n)
        vector<int> prev(n,0);
        for(int i = 0; i < m; i++){
            vector<int> cur(n,0);
            for(int j = 0; j < n; j++){
                if(i==0 && j==0) cur[j] = 1;
                else{
                    int up = 0;
                    int left = 0;
                    if(i > 0) up = prev[j];
                    if(j > 0) left = cur[j-1];
                    cur[j] = up + left;
                }
            }
            prev = cur;
        }
        return prev[n-1];
        //BY Tabulation
        //TC - O(n*m) and SC - O(n*m)
        /*
        vector<vector<int>> dp(m, vector<int> (n,-1));
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(i==0 && j==0)dp[i][j] = 1;
                else{
                    int up = 0;
                    int left = 0;
                    if(i > 0) up = dp[i-1][j];
                    if(j > 0) left = dp[i][j-1];
                    dp[i][j] = up + left;
                }
            }
        }
        return dp[m-1][n-1];
        */ 


        //By Recursiob DP and Memoization
        //Top Down
        //TC - O(n*m) amd SC - O(m + n + m*n)
        /*
        vector<vector<int>> dp(m,vector<int> (n,-1));
        return solve(m-1, n-1 , dp);
        */

    }
};