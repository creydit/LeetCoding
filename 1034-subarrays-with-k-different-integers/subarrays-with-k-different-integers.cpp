class Solution {
public:
    int solve(vector<int> &nums, int k){
        //TC - O(2n)
        int n = nums.size();
        int r = 0;
        int l = 0;
        map<int, int>mpp;
        int ans = 0;
        while( r < n){
            mpp[nums[r]]++;
            while(mpp.size() > k){
                mpp[nums[l]]--;
                if(mpp[nums[l]] == 0) mpp.erase(nums[l]);
                l++;
            }
            ans += r - l + 1;
            r++;
        }
        return ans;
    }
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        //Optimal by sliding window 
        //TC - O(4*n) and SC - O(n)
        return solve(nums, k) - solve(nums, k-1);

        
        //Brute force using 2 loops 
        //TC - O(n2) and SC - O(n)
        /*
        int n = nums.size();
        int ans = 0;
        for(int i = 0; i < n; i++){
            map<int,int> mpp;
            for(int j = i; j < n ; j++){
                mpp[nums[j]]++;
                if(mpp.size() == k) ans++;
                else if (mpp.size() > k) break;
            }
        }
        return ans;
        */
    }
};