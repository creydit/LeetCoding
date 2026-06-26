class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int,int> mpp;
        mpp[0] = 1;
        int ans = 0;
        int ss = 0;
        for(int i = 0; i < n; i++){
            ss += nums[i];
            ans += mpp[ss - k];
            mpp[ss] += 1;
        }
        return ans;
    }
};