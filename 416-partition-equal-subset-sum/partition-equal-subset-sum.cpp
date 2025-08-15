class Solution {
public:
    bool solve(int n, vector<int> &arr, int target){
        vector<bool> prev(target + 1, false), curr(target + 1, false);
        prev[0] = curr[0] = true;
        if(arr[0] <= target) prev[arr[0]] = true;
        for(int i = 1; i < n; i++){
            for(int j = 1; j <= target; j++){
                bool ntake = prev[j];
                bool take = false;
                if (arr[i] <= j) take = prev[j - arr[i]];
                
                curr[j] = ntake | take;
            }
            prev = curr;
        }
        return prev[target];
    }
    bool canPartition(vector<int>& nums) {
        //by using logic we are finding the total sum and checking if it is divisible by 2 then we can 
        //partition by into two otherwise we cannot 
        //and lets say S be the total sum then sum of one subset will be S/2 therefore our task boils down 
        //to finding a subset with sum of S/2 and if its there then our answer is true
        //TC - O(n * sum(n)/2) and SC - O(sum)
        int n = nums.size();
        int sum = 0;
        for(int i = 0; i < n; i++){
            sum += nums[i];
        }
        if (sum % 2) return false;
        return solve(n, nums, sum/2);
    }
};