class Solution {
public:
    /*
    int solve(int r, int c, vector<vector<int>>& matrix, int &n, int &m,  vector<vector<int>>& dp){
        if (c < 0 || c >= m) return 1e9;
        if (r == 0) return matrix[r][c];
        if(dp[r][c] != -1) return dp[r][c];
        int up = matrix[r][c] + solve(r - 1, c, matrix, n, m, dp);
        int ld = matrix[r][c] + solve(r - 1, c - 1, matrix, n, m, dp);
        int rd = matrix[r][c] + solve(r - 1, c + 1, matrix, n, m, dp);
        int ans = min(ld,rd);
        ans = min(ans, up);
        return dp[r][c] = ans;
    }
    */
    int minFallingPathSum(vector<vector<int>>& matrix) {
        //Tabulation //Bottom Up
        //TC - O(n*m) and SC - O(n*m)
        int n = matrix.size();
        int m = matrix[0].size();
        vector<vector<int>> dp(n, vector<int>(m, -1));
        for(int j = 0; j < m; j++) {
            dp[0][j] = matrix[0][j];
        }

        for(int i = 1; i < n; i++){
            for(int j = 0; j < m; j++){
                int up = matrix[i][j] + dp[i - 1][j];
                int ld = matrix[i][j];
                ld += j-1 >= 0 ? dp[i - 1][j - 1] : 1e9;
                int rd = matrix[i][j];
                rd += j+1 < m ? dp[i - 1][j + 1] : 1e9;
                int ans = min(ld,rd);
                dp[i][j]= min(ans, up);
            }
        }
        int ans = INT_MAX;
        for (int j = 0; j < m; j++){
            ans = min(ans, dp[n-1][j]);
        }
        return ans;

        //Recursive  + Dp + Memoization //Top Down
        // TC - O(n*m) and SC - O(n*m + n)
        /*
        int n = matrix.size();
        int m = matrix[0].size();
        vector<vector<int>> dp(n, vector<int>(m, -1));
        int ans = INT_MAX;
        for(int j = 0; j < m; j++){
            ans = min(ans, solve(n-1, j, matrix, n, m, dp));
        }
        return ans;
        */
    }
};