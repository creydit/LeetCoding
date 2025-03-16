class Solution {
public:
    //Optimal by Binary Search TC- O(n logn(max-min+1) from bloomDay)
    int poss(vector<int>& arr,int day,int m,int k){
        int numofB=0;
        int cnt=0;
        for(int i=0;i<arr.size();i++){
            if(arr[i]<=day){
                cnt++;
            }
            else{
                numofB+=(cnt/k);
                cnt=0;
            }
        }
        numofB+=(cnt/k);
        if (numofB>=m)return true;
        else return false;
    }
    int minDays(vector<int>& bloomDay, int m, int k) {
        int n=bloomDay.size();
        long long q = (m*1LL)*(1LL*k);
        if(q>n)return -1;
        int low=1;
        int high=0;
        for(int i=0;i<n;i++){
            low=min(low,bloomDay[i]);
            high=max(high,bloomDay[i]);
        }
        int ans=0;
        while(low<=high){
            int mid=(low+high)/2;
            if(poss(bloomDay,mid,m,k)){
                ans=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return ans;
    }
    //linear search can also be applied but TC-O(n2)
};