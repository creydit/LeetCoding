class Solution {
public:
    //Optimal by Binary Search TC-O(n* log(max-sum of nums)) (Same Problem as Book Allocation)
    int func(vector<int> &arr,int mid){
        int num=1;
        long long sum=0;
        for(int i=0;i<arr.size();i++){
            if(arr[i]+sum<=mid){
                sum+=arr[i];
            }else{
                num+=1;
                sum=arr[i];
            }
        }
        return num;
    }
    int splitArray(vector<int>& nums, int k) {
        int n=nums.size();
        int low=0;
        int high=0;
        for(auto i:nums){
            low=max(low,i);
            high+=i;
        }
        while(low<=high){
            int mid=(low+high)/2;
            if(func(nums,mid)>k){
                low=mid+1;
            }else{
                high=mid-1;
            }
        }
        return low;
    }
};