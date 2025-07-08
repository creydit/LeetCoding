class Solution {
public: 
    int dp[1001];
    int solve(int sum, vector<int> &nums, int target){
        if( sum == target) return 1;
        if(sum > target) return 0;
        if(dp[sum] != -1) return dp[sum];

        int res = 0;
        for(int i = 0; i < nums.size(); i++){; 
            res += solve(sum+nums[i], nums, target);
        }
        return dp[sum] = res;
    }
    int combinationSum4(vector<int>& nums, int target) {
        //Recursion and Backtracking 
        //TC - O(2^n)
        //Gives tle on raw recursion therefore using dp woth memoization
        //with tat this Qs marks as my first DP solution
        //TC - O(target * len(nums))
        memset(dp, -1, sizeof(dp));
        return solve(0, nums, target);
    }
};