class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        //From Editorial Learning
        int ans=0;
        unordered_map<int,int>mpp;
        for(int i=0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                int p=nums[i]*nums[j];
                mpp[p]++;
            }
        }
        for(auto [x,y]:mpp){
            int equal= y*(y-1)/2;
            ans+=(equal*8);
        }
        return ans;
        
        //FTS By me, POTD
        /*
        int ans=0;
        unordered_map<int,int>mpp;
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
        */
    }
};