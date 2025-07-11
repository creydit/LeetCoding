class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        //Better solution uses 2 pointer and sliding window approach 
        //Tc - O(n+n) ~ O(2n) due to ineer while loop and SC - O(1)
        int n = nums.size();
        int ans = 0;
        int l = 0;
        int r = 0;
        int zero = 0;
        while( r < n ){
            if (nums[r] == 0) zero++;

            while( zero > k){
                if(nums[l] == 0) zero--;
                l++;
            }

            if (zero <= k){
                ans = max(ans, r - l + 1);
            }
            r++;
        }
        return ans;

        //Brute force using 2 loops and finding all the subarrays 
        //Also converting the question to finding the max length of array with atmost  k zeros
        //as converting those k zeros will make us the longest consecutive ones
        //TC - O(n2) and SC - O(1)
        /*
        int n = nums.size();
        int ans = 0;
        for(int i = 0; i < n; i++){
            int zero = 0;
            for(int j = i; j < n; j++){
                if (nums[j] == 0) zero++;
                if( zero <= k){
                    ans = max(ans, j - i + 1);
                }
                else break;
            }
        }
        return ans;
        */
    }
};