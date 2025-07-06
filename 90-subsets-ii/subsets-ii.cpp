class Solution {
public:
    void solve(int ind, vector<vector<int>> &ans, vector<int> temp, vector<int> nums){
        if(ind>=nums.size()){
            ans.push_back(temp);
            return;
        }
        temp.push_back(nums[ind]);
        solve(ind+1, ans, temp, nums);
        temp.pop_back();

        //skipping duplicate elements 
        while(ind+1 < nums.size() && nums[ind] == nums[ind+1]){
            ind++;
        }
        solve(ind+1, ans, temp, nums);
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        //Recursion and Backtracking approach with condition to check if temp already exist in ans
        //TC - O(2^n * n) and SC - O(n) depth of recursion
        vector<vector<int>> ans;
        vector<int> temp;
        sort(nums.begin(),nums.end());
        solve(0, ans, temp, nums);
        return ans;
    }
};