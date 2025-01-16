class Solution {
public:
    int maxProduct(vector<int>& nums) {
        //Optimal Sol by perifx and suffix calculation
        int n=nums.size();
        int ans=INT_MIN;
        int pref=1;
        int suf=1;
        for(int i=0;i<n;i++){
            if(pref==0)pref=1;
            if(suf==0)suf=1;
            pref*=nums[i];
            suf*=nums[n-i-1];
            ans=max(ans,max(pref,suf));
        }
        return ans;

        //Brute Force O(n2)
        /*
        int n=nums.size();
        int ans=INT_MIN;
        for(int i=0;i<n;i++){
            int currpro=1;
            for(int j=i;j<n;j++){
                currpro*=nums[j];
                ans=max(ans,currpro);
            }
        }
        return ans;
        */
    }
};