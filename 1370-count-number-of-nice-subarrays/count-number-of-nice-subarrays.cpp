class Solution {
public:
    int solve(vector<int>& nums, int k){
        if(k  < 0) return 0;
        int n = nums.size();
        int l = 0;
        int r = 0;
        int ans = 0;
        int odds = 0;
        while( r < n){
            if (nums[r]%2 == 1) odds++;
            while(odds > k){
                if(nums[l]%2 == 1){
                    odds--;
                }
                l++;
            }
            ans = ans + (r - l + 1);
            r++;
        }
        return ans;
    }
    int numberOfSubarrays(vector<int>& nums, int k) {
        //Optimal approach involves sliding window approach
        //TC - O(2 * 2n) and SC - O(1)
        return solve(nums, k) - solve(nums, k-1);

        //Brute force is using two loops for finding every sub array and then counting the number of odd
        //in this and updating the ans if they equal to k 
        // TC - O(n^2) and  SC - O(1)
        /*
        int n = nums.size();
        int ans  = 0;
        for(int i = 0; i < n; i++){
            int odds = 0;
            for(int j = i; j < n; j++){
                if(nums[j]%2 == 1){
                    odds++;
                }
                if(odds == k){
                    ans++;
                }
            }
        }
        return ans;
        */
    }
};