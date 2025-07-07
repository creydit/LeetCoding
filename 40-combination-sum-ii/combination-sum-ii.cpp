class Solution {
public:
    vector<vector<int>> ans;
    void solve(int idx, int sum, vector<int>& cand, vector<int> temp, int target){
        if( sum == target){
            ans.push_back(temp);
            return;
        }
        if(sum > target){
            return;
        }
        for(int i = idx; i < cand.size(); i++){
            if(i > idx && cand[i] == cand[i-1])continue;
            if(sum + cand[i] > target) break;
            temp.push_back(cand[i]);
            solve(i+1, sum + cand[i], cand, temp, target);
            temp.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        //Recursion and Backtracking
        //TC - O(2^t * k)
        sort(candidates.begin(),candidates.end());
        vector<int> temp;
        solve(0, 0, candidates, temp, target);
        return ans;
    }
};