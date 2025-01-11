class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        //By ME (nlogn)
        int n=nums.size();
        map<int,int>mpp;
        vector<int>ans;
        int c=(n/3)+1;
        for(auto i:nums){
            mpp[i]++;
            if(mpp[i]==c)ans.push_back(i);
        }
        return ans;
    }
};