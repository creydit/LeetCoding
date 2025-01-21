class Solution {
public:
    int FirstOcc(vector<int>& arr,int t){
        int low=0;
        int high=arr.size()-1;
        int fo=-1;
        while(low<=high){
            int mid=(low+high)/2;
            if(arr[mid]==t){
                fo=mid;
                high=mid-1;
            }
            else if(arr[mid]>t){
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return fo;
    }

    int LastOcc(vector<int>& arr,int t){
        int low=0;
        int high=arr.size()-1;
        int lo=-1;
        while(low<=high){
            int mid=(low+high)/2;
            if(arr[mid]==t){
                lo=mid;
                low=mid+1;
            }
            else if(arr[mid]>t){
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return lo;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        //By me and Binary Search
        int first=FirstOcc(nums,target);
        if(first==-1)return {-1,-1};
        int last=LastOcc(nums,target);
        return {first,last};

        //Can be by using lowerbound and upperbound

        //FTS by me, See Submission for date
        /*
        vector<int>a(2,-1);
        if(find(nums.begin(),nums.end(),target)==nums.end()){
            return a;
        }
        else{
            vector<int>ans;
            for(int i=0;i<nums.size();i++){
                if(nums[i]==target){
                    ans.push_back(i);
                    break;
                }
            }
            for (int i=nums.size()-1;i>=0;--i){
                if(nums[i]==target){
                    ans.push_back(i);
                    break;
                }
            }
            return ans;
        }
        */
    }
};