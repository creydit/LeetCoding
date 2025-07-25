class Solution {
public:
    int maxSum(vector<int>& nums) {
        //Simple traversal + checking 
        // TC - O(n) and SC - O(101)
        int ans = 0;
        vector<int> hash(101);
        int maxi = INT_MIN;
        for(auto i : nums){
            if ( i > 0 && hash[i] == 0){
                ans += i;
                hash[i]++;
            } 
            maxi = max(maxi, i);
        }
        if (ans == 0) return maxi;
        return ans;
    }
};