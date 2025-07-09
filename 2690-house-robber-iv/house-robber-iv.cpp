class Solution {
public:
    int helper(int mid, vector<int> nums, int  k){
        int n = nums.size();
        int noOfH = 0;
        int i = 0;
        while( i < n){
            if(nums[i] <= mid){
                noOfH++;
                i+=2;
            }
            else{
                i+=1;
            }
        }
        if(noOfH >= k)return true;
        return false;
    }

    int minCapability(vector<int>& nums, int k) {
        //Optimal by Binary search from one to highest element then checking if he can steal from the 
        //housed not adjacent for every mid value respectively
        //TC - O( n * log(max - min)) and SC - O(1)
        int low = 1;
        int high = *max_element(nums.begin(),nums.end());
        int ans = 0;
        while(low <= high){
            int mid = (low + high)/2;
            if(helper(mid,nums,k)){
                ans = mid;
                high = mid -1;
            }
            else{
                low = mid + 1;
            }
        }
        return ans;
    }
};