class Solution {
public:
    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();

        vector<long long> ps(n + 1, 0);
        for (int i = 0; i < n; i++) {
            ps[i + 1] = ps[i] + stoneValue[i];
        }

        vector<vector<int>> dp(n, vector<int>(n, 0));

        for (int length = 1; length < n; length++) {
            for (int l = 0; l < n - length; l++) {

                int r = l + length;

                for (int k = l; k < r; k++) {

                    long long ls = ps[k + 1] - ps[l];
                    long long rs = ps[r + 1] - ps[k + 1];

                    if (ls > rs) {
                        dp[l][r] = max(
                            dp[l][r],
                            (int)(rs + dp[k + 1][r])
                        );
                    }
                    else if (rs > ls) {
                        dp[l][r] = max(
                            dp[l][r],
                            (int)(ls + dp[l][k])
                        );
                    }
                    else {
                        dp[l][r] = max(
                            dp[l][r],
                            (int)(ls + max(dp[l][k], dp[k + 1][r]))
                        );
                    }
                }
            }
        }

        return dp[0][n - 1];
    }
};