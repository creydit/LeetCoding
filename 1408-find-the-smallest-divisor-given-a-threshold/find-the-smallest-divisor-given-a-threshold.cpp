class Solution {
public:
    //Optimal By Binary Search (by me) TC-O(n log(max(nums)))
    bool func(vector<int>& arr,int m,int t){
        int sum=0;
        for(auto i:arr){
            sum+=ceil(double(i)/double(m));
        }
        if (sum<=t)return true;
        else return false;
    }
    int smallestDivisor(vector<int>& nums, int threshold) {
        int n=nums.size();
        if(n>threshold)return -1; //Case when answer will not exist(Not asked in this Qs)
        int low=1;
        int high=0;
        for(int i=0;i<n;i++){
            high=max(high,nums[i]);
        }
        int ans=0;
        while(low<=high){
            int mid=(low+high)/2;
            if(func(nums,mid,threshold)){
                ans=mid;
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return ans;
    }
};