class Solution {
public:
    //Optimal by Binary Search TC-O(n * log( sum(weights) - max(weights) ))
    bool func(vector<int> &arr,int m,int d){
        int days=1;
        int load=0;
        for(int i=0;i<arr.size();i++){
            if(load+arr[i]>m){
                days+=1;
                load=arr[i];
            }else{
                load+=arr[i];
            }
        }
        if(days<=d)return true;
        else return false;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int n=weights.size();
        int low=0;
        int high=0;
        for(auto i : weights){
            low=max(low,i);
            high+=i;
        }
        while(low<=high){
            int mid=(low+high)/2;
            if(func(weights,mid,days)){
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return low;

    }
};