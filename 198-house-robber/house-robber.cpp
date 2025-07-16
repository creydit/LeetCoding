class Solution {
public:
    /*
    int solve(int idx, int ans, vector<int> nums, vector<int> &dp){
        if(idx >= nums.size()){
            return 0;
        }
        if(dp[idx] != -1) return dp[idx];
        int l = nums[idx] + solve(idx+2, ans, nums, dp);
        int r = solve(idx+1, ans, nums, dp);
        return dp[idx] = max(l,r);
    }
    */
    int rob(vector<int>& nums) {
        //using logic and math 
        //TC - O(n) and SC - O(1)
        int prev2 = 0;
        int prev = nums[0];
        for(int i = 1; i < nums.size(); i++){
            int take = nums[i];
            if( i > 1) take += prev2;
            int nottake = 0 + prev;

            int curi = max(take, nottake);
            prev2 = prev;
            prev = curi;
        }
        return prev;

        //other way of writing above code -
        /*
        int a,b,c =0;
        for(int i = 0; i < nums.size(); i++){
            int d = max(a,b) + nums[i];
            a = b;
            b = c;
            c = d;
        }
        return max(b,c);
        */

        //Recursion and Backtracking
        //TC - O(2^n)
        //Using DP and improving the solution 
        //still not optimal of spaced optimised DP
        //TC - O(n) and SC - O(n)
        /*
        int n = nums.size();
        vector<int> dp(n,-1);
        return solve(0, 0, nums, dp);
        */
    }
};