class Solution {
public:
    int maxSum(vector<int>& nums) {
        //Simple traversal + checking 
        // TC - O(n) and SC - O(101)
        int ans = 0;
        vector<int> hash(101);
        for(auto i : nums){
            if ( i > 0 && hash[i] == 0){
                ans += i;
                hash[i]++;
            } 
        }
        if (ans == 0){
            ans = INT_MIN;
            for(auto i : nums){
                ans = max(ans, i);
            }
        }
        return ans;
    }
};