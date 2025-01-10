class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        //Optimal by map and reverse eng
        map<int,int>mpp;
        mpp[0]=1;
        int presum=0,cnt=0;
        for(int i=0;i<nums.size();i++){
            presum+=nums[i];
            int rem=presum-k;
            cnt+=mpp[rem];
            mpp[presum]++;
        }
        return cnt;
        //Brute Force by 2 loops
    }
};