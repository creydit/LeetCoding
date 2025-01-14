class Solution {
private:
    void swapIfGreater(vector<int>& a1, vector<int>& a2,int idx1,int idx2){
        if(a1[idx1]>a2[idx2]){
            swap(a1[idx1],a2[idx2]);
        }
    }
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        //Optimal 1 by comparing the largest and smallest of both arrays and sorting all
        //TC - min(n,m)+nlogn+mlogm , SC-O(1)
        /*
        int left=m-1;
        int right=0;
        while(left>=0 && right<n){
            if(nums1[left]>nums2[right]){
                swap(nums1[left],nums2[right]);
                left--;
                right++;
            }else{
                break;
            }
        }
        sort(nums1.begin(),nums1.begin()+m);
        sort(nums2.begin(),nums2.end());
        for(int i=m;i<n+m;i++){
            nums1[i]=nums2[i-m];
        }
        */
        
        //Optimal 2 by Gap method and Shell sort
        //TC- (n+m)log(n+m) SC-O(1)
        int l=n+m;
        int gap=l/2 + (l%2);
        while(gap>0){
            int left=0;
            int right=left + gap;
            while(right<l){
                if(left<m && right>=m) swapIfGreater(nums1,nums2,left,right-m); //nums1 , nums2
                else if(left>=m) swapIfGreater(nums2,nums2,left-m,right-m); //nums2,nums2
                else swapIfGreater(nums1,nums1,left,right); //nums1 , nums1
                left++;
                right++;
            }
            if(gap==1)break;
            gap=gap/2+(gap%2);
        }
        for(int i=m;i<n+m;i++){
            nums1[i]=nums2[i-m];
        }

        //Brute Force by Merge func of merge sort TC-n+m SC=n+m
        /*
        vector<int>arr3(n+m,0);
        int left=0;
        int right=0;
        int index=0;
        while(left<m && right<n){
            if(nums1[left]<=nums2[right]){
                arr3[index]=nums1[left];
                left++;
                index++;
            }else{
                arr3[index]=nums2[right];
                right++;
                index++;
            }
        }
        while(left<m){
            arr3[index]=nums1[left];
            index++;
            left++;
        }
        while(right<n){
            arr3[index]=nums2[right];
            index++;
            right++;
        }
        for(int i=0;i<m+n;i++){
            nums1[i]=arr3[i];
        }
        */
    }
};