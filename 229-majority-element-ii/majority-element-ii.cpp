class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        //By ME
        int n=nums.size();
        map<int,int>mpp;
        for(auto i:nums){
            mpp[i]++;
        }
        vector<int>ans;
        int c=n/3;
        for(auto x:mpp){
            if (x.second>c)ans.push_back(x.first);
        }
        return ans;
    }
};