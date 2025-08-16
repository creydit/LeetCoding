class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans;
        vector<int> pref;
        vector<int> suff;
        pref.push_back(nums[0]);
        suff.push_back(nums[n-1]);
        for(int i = 1; i < n; i++){
            pref.push_back(pref[i-1]*nums[i]);
        }
        for(int i = 1; i < n; i++){
            suff.push_back(suff[i-1]*nums[n-i-1]);
        }
        reverse(suff.begin(),suff.end());
        for(int i = 0; i < n; i++){
            if (i == 0){
                ans.push_back(suff[i+1]);
                continue;
            }
            if(i == n-1){
                ans.push_back(pref[i-1]);
                continue;
            }
            ans.push_back((suff[i+1]*pref[i-1]));
        }
        return ans;


        /*
        for(int i = 0; i< n; i++){
            int pro = 1;
            for(int j = 0; j < n; j++){
                if(i==j) continue;
                pro*=nums[j];
            }
            ans.push_back(pro);
        }
        return ans;
        */
    }
};