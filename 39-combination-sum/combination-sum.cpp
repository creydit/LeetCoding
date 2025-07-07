class Solution {
public:
    vector<vector<int>>ans;
    void solve(int idx, vector<int>& cand, vector<int>temp, int target){
        if(idx == cand.size()){
            if(target == 0){
                ans.push_back(temp);
            }
            return;
        }
        if(cand[idx] <= target){
            temp.push_back(cand[idx]);
            solve(idx, cand, temp, target - cand[idx]);
            temp.pop_back();
        }
        solve(idx+1, cand, temp, target);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        //Recursion and Backtracking 
        //TC - (2^t * k) 
        vector<int>temp;
        solve(0, candidates, temp, target);
        return ans;
    }
};