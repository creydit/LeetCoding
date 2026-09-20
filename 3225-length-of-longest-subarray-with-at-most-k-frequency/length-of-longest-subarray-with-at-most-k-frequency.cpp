class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int,int> mpp;
        int ans = 0;
        int l = 0;
        for(int r = 0; r < n; r++){
            mpp[nums[r]]+=1;
            while (mpp[nums[r]] > k){
                mpp[nums[l]] -= 1;
                l += 1;
            }
            ans = max(ans, r-l+1);
        }
        return ans;
    }
};