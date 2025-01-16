#define ll long long
class Solution {
public:
    void merge(vector<int>&a,int low,int mid,int high){
        vector<int>ans;
        int left=low;
        int right=mid+1;
        while(left<=mid && right<=high){
            if(a[left]<a[right]){
                ans.push_back(a[left]);
                left++;
            }else{
                ans.push_back(a[right]);
                right++;
            }
        }
        while(left<=mid){
            ans.push_back(a[left]);
            left++;
        }
        while(right<=high){
            ans.push_back(a[right]);
            right++;
        }
        for(int i=low;i<=high;i++){
            a[i]=ans[i-low];
        }
    }
    int countpair(vector<int>&a,int low,int mid,int high){
        int cnt=0;
        int j=mid+1; // right==j
        for(int i=low;i<=mid;i++){
            while(j<=high && (long long)(a[i])>(long long)(2*(long long
            )a[j])){
                j++;
            }
            cnt+=(j-(mid+1));
        }
        return cnt;
    }
    int mergesort(vector<int>&a, int low,int high){
        int cnt=0;
        if(low>=high) return cnt;
        int mid=(low+high)/2;
        cnt+=mergesort(a,low,mid);
        cnt+=mergesort(a,mid+1,high);
        cnt+=countpair(a,low,mid,high);
        merge(a,low,mid,high);
        return cnt;
    }
    int reversePairs(vector<int>& nums) {
        //Optimal by merge sort algorithm
        return mergesort(nums,0,nums.size()-1);
        //Brtue Force O(n2)
        /*
        int n=nums.size();
        int ans=0;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(nums[i]>2*nums[j])ans++;
            }
        }
        return ans;
        */
    }
};