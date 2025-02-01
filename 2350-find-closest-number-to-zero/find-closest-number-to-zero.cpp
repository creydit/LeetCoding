class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        //FTS BY ME
        int ans;
        int dist=INT_MAX;
        for(auto i:nums){
            int x=abs(i);
            if (dist>=x){
                if(ans==x){
                    continue;
                }
                ans=i;
                dist=x;
            }
        }
        return ans;
    }
};