class Solution {
public:
    /*
    int solve(int i, int j, vector<vector<int>> &tri, vector<vector<int>> &dp){
        if(i == tri.size() - 1) return tri[i][j];
        if(dp[i][j] != -1) return dp[i][j];

        int d = tri[i][j] + solve(i+1, j, tri, dp);
        int dg = tri[i][j] + solve(i+1, j+1, tri, dp);

        return dp[i][j] = min(d,dg);
    }
    */

    int minimumTotal(vector<vector<int>>& triangle) {
        //By Tabulation
        //TC - O(n*n) and SC - O(n*n)
        int n = triangle.size();
        vector<vector<int>>dp(n, vector<int>(n, -1));
        for(int j = 0; j < n; j++){
            dp[n-1][j] = triangle[n-1][j];
        }
        for(int i = n-2; i>=0; i--){
            for(int j = i; j>=0; j--){
                int d = triangle[i][j] + dp[i+1][j];
                int dg = triangle[i][j] + dp[i+1][j+1];
                dp[i][j] = min(d,dg);
            }
        }
        return dp[0][0];
 
        //Recursion + DP with memoization
        //TC - O(n*n) and SC - (n+n+n*n)
        /*
        int n = triangle.size();
        vector<vector<int>>dp(n, vector<int>(n, -1));
        return solve(0,0, triangle, dp);
        */
    }
};