class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        //iterating through and counting the numbers not equal to val then 2 pointer to make all the 
        //numbers not equal to val place at the last 
        //TC - O(n + n) and SC - O(1)
        int n = nums.size();
        int ans = 0;
        for(int i = 0; i < n; i++){
            if(nums[i] != val){
                ans++;
            }
        }
        int i = 0;
        int j = nums.size() - 1;
        while(i <= j){
            if (nums[i] == val) {
                while (j > i && nums[j] == val) j--;
                if (i >= j) break;
                swap(nums[i], nums[j]);
                j--;
            }
            i++;
        }
        return ans;
    }
};