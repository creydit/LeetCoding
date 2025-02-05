class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        //FTS, By Seeing Solution and Understanding it 
        //Understanding Help - codestorywithMIK 
        //Fully Observation based question
        long long maxReach=0;
        int ans=0;
        int i=0;
        while(maxReach<n){
            if(i<nums.size() && nums[i]<=maxReach+1){
                maxReach+=nums[i];
                i++;
            }
            else{
                maxReach+=(maxReach+1);
                ans++;
            }
        }
        return ans;
    }
};