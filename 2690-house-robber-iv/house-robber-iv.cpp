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
        int low = *min_element(nums.begin(),nums.end());
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