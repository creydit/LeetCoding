class Solution {
public:
    int solve(int idx, int ans, vector<int> nums, vector<int> &dp){
        if(idx >= nums.size()){
            return 0;
        }
        if(dp[idx] != -1) return dp[idx];
        int l = nums[idx] + solve(idx+2, ans, nums, dp);
        int r = solve(idx+1, ans, nums, dp);
        return dp[idx] = max(l,r);
    }
    int rob(vector<int>& nums) {
        //Recursion and Backtracking
        //TC - O(2^n)
        //Using DP and improving the solution 
        //still not optimal of spaced optimised DP
        //TC - O(n) and SC - O(n)
        int n = nums.size();
        vector<int> dp(n,-1);
        return solve(0, 0, nums, dp);
    }
};