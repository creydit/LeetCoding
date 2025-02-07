class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        //FTS By me, POTD
        int ans=0;
        map<int,int>mpp;
        for(int i=0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                int p=nums[i]*nums[j];
                if(mpp.find(p)!=mpp.end()){
                    ans+=mpp[p];
                }
                mpp[p]++;
            }
        }
        return ans*8;
    }
};