class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        //Optimal apporach by sliding window 
        //TC - O(n) and SC - O(max(nums))
        int n = nums.size();
        int ans = 0;
        int l = 0;
        int r = 0;
        int sum = 0;
        vector<int> hash(1e4 + 1, 0);
        while( r < n){
            while(hash[nums[r]] == 1){
                hash[nums[l]] = 0;
                sum -= nums[l];
                l++;
            }
            sum += nums[r];
            hash[nums[r]] = 1;
            ans = max(ans, sum);
            r++;
        }
        return ans;
        //Brute force using 2 loops and making hash map
        //TC - O(n2) and SC - O(max(nums))
        /*
        int n = nums.size();
        int ans = 0;
        for(int i = 0; i < n; i++){
            int sum = 0;
            vector<int> hash(1e4 + 1, 0);
            for(int j = i; j < n; j++){
                if(hash[nums[j]] == 1){
                    break;
                }
                hash[nums[j]] = 1;
                sum += nums[j];
            }
            ans = max(ans, sum);
        }
        return ans;
        */
    }
};