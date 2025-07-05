class Solution {
public:
    void solve(int ind, vector<vector<int>> &ans, vector<int> &nums, vector<int> arr){
        if(ind>=nums.size()){
            ans.push_back(arr);
            return;
        }

        solve(ind+1, ans, nums, arr); //not take condition
        arr.push_back(nums[ind]);
        solve(ind+1, ans, nums, arr); //take condition
        arr.pop_back();
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        //Recursion and Backtracking with a take and not take condition over the elements to find
        //all the subsequences
        //TC - O(2^n) and SC - O(n) depth of recursion
        vector<vector<int>> ans;
        vector<int> arr;
        solve(0,ans,nums,arr);
        return ans;
    }
};