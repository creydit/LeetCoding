class Solution {
public:
    /*
    int solve(int idx, int sum, vector<int>& nums, vector<vector<int>> &dp){
        if(idx == 0){
            if (sum == 0 && nums[0] == 0) return 2;
            if (sum == 0) return 1;
            if(nums[0] == sum) return 1;
            return 0;
        }
        if(dp[idx][sum] != -1) return dp[idx][sum];

        int nottake = 0 + solve(idx - 1, sum, nums,dp);
        int take = 0;
        if(nums[idx] <= sum) take += solve(idx - 1, sum - nums[idx], nums, dp);

        return dp[idx][sum] = take + nottake;
    }
    */
    int tabu(vector<int> nums, int target){
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(target + 1, 0));
        if(nums[0] == 0) dp[0][0] = 2;
        else{
            dp[0][0] = 1;
            if(nums[0] <= target) dp[0][nums[0]] = 1;
        }
        for(int idx = 1; idx < n; idx++){
            for(int sum = 0; sum <= target; sum++){
                int nottake = 0 + dp[idx - 1][sum];
                int take = 0;
                if(nums[idx] <= sum) take += dp[idx - 1][sum - nums[idx]];

                dp[idx][sum] = take + nottake;
            }
        }
        return dp[n-1][target];
    }
    int findTargetSumWays(vector<int>& nums, int target) {
        //By deducing this problem becomes "Partitions with Given Difference" and so does the code
       
        int totsum = 0;
        for(auto i : nums) totsum += i;
        if(totsum - target < 0 || (totsum - target) % 2 != 0) return 0;
        int n = nums.size();
        int newTarget = (totsum - target) / 2;
        
        //BY Tabulation
        //TC - O(n*target) and SC - O(n*target)
        return tabu(nums, newTarget);

        //By Recursion + DP + Memoization
        //Tc - O(n*target) and SC - O(n*target + n)
        /*
        vector<vector<int>> dp(n, vector<int> (newTarget+1 , -1));
        return solve(n-1, newTarget, nums, dp);
        */

    }
};