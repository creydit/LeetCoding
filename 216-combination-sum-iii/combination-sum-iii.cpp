class Solution {
public:
    vector<vector<int>> ans;
    void solve(int idx, int sum, vector<int> &cand, vector<int> temp, int n, int k){
        if( sum == n){
            if(temp.size() == k){
                ans.push_back(temp);
            }
            return;
        }
        if(sum > n){
            return;
        }
        for(int i = idx; i < cand.size(); i++){
            if(sum + cand[i] > n) break;
            temp.push_back(cand[i]);
            solve(i+1, sum+cand[i], cand, temp, n, k);
            temp.pop_back();
        }
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        //Recursion and Backtracking
        //TC - O(2^n * n)
        vector<int> cand = {1,2,3,4,5,6,7,8,9};
        vector<int> temp;
        solve(0, 0, cand, temp, n, k);
        return ans;
    }
};