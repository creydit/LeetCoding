class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        //Optimal By Binary Search O(logn)
        int n=nums.size();
        int low=1;
        int high=n-2;
        if(n==1)return nums[0];
        if(nums[0]!=nums[1])return nums[0];
        if(nums[n-1]!=nums[n-2])return nums[n-1];
        while(low<=high){
            int mid=(low+high)/2;
            if(nums[mid]!=nums[mid+1] && nums[mid]!=nums[mid-1]){
                return nums[mid];
            }
            //We're in left half
            if( (mid%2==1 && nums[mid]==nums[mid-1]) || (mid%2==0 && nums[mid]==nums[mid+1]) ){
                low=mid+1; //Going in to Right Half
            }
            else{ //We're in Right Half
                high=mid-1; //Going in to Left Half
            }
        }
        return 0;

        //Brute Force by Linearly O(n)
        /*
        int n=nums.size();
        if(n==1)return nums[0];
        for(int i=0;i<n;i++){
            if(i==0){
                if(nums[i]!=nums[i+1]){
                    return nums[i];
                }
            }
            else if(i==n-1){
                if(nums[i]!=nums[i-1]){
                    return nums[i];
                }
            }
            else{
                if(nums[i]!=nums[i+1] && nums[i]!=nums[i-1]){
                    return nums[i];
                }
            }
        }
        return 0;
        */
    }
    
};