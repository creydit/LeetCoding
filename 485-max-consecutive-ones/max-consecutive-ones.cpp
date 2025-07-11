class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        //Basic traversal and updating ans if nums[i] == 1 and making curr = 0 if nums[i] == 0
        //TC - O(n) and SC - O(1)
        int ans = 0;
        int n = nums.size();
        int curr = 0;
        for(int i = 0; i < n; i++){
            if (nums[i] == 0) curr = 0;
            else{
                curr++;
                ans = max(ans, curr);
            }
        }
        return ans;
    }
};