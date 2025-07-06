class Solution {
public:
    void solve(int ind, vector<vector<int>> &ans, vector<int> temp, vector<int> nums){
        ans.push_back(temp);

       for(int i=ind; i<nums.size(); i++){
            if(i>ind && nums[i] == nums[i-1])
            continue;

            temp.push_back(nums[i]);
            solve(i+1, ans, temp, nums);
            temp.pop_back();
        }

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