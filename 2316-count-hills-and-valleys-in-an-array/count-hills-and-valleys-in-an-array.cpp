class Solution {
public:
    int countHillValley(vector<int>& nums) {
        int n = nums.size();
        int prev = 0;
        int curr = 1;
        int front = 2;
        int ans = 0;
        while ( front < n){
            if( nums[curr] == nums[front] ){
                curr++;
                front++;
                continue;
            }
            if( nums[prev] < nums[curr] && nums[front] < nums[curr]) ans++;
            else if (nums[prev] > nums[curr] && nums[front] > nums[curr] ) ans++;
            curr++;
            front++;
            prev = curr - 1;
        }
        return ans;
    }
};