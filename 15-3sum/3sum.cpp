class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n=nums.size();
        //Optimal Solution Two pointers TC-O(n2+nlogn) SC-O(no of triplets)
        vector<vector<int>>ans;
        sort(nums.begin(),nums.end());
        for(int i=0;i<n;i++){
            if(i>0 && nums[i]==nums[i-1])continue;
            int j=i+1;
            int k=n-1;
            while(j<k){
                int s=nums[i]+nums[j]+nums[k];
                if(s<0){
                    j++;
                }
                else if(s>0){
                    k--;
                }
                else{
                    vector<int>temp={nums[i],nums[j],nums[k]};
                    ans.push_back(temp);
                    j++;
                    k--;
                    while(j<k && nums[j]==nums[j-1])j++;
                    while(j<k && nums[k]==nums[k+1])k--;
                }
            }
        }
        return ans;

        //Better by using hash O(~n2logn)
        /*
        set<vector<int>>ans1;
        for(int i=0;i<n;i++){
            set<int>hashset;
            for(int j=i+1;j<n;j++){
                int rem=-(nums[i]+nums[j]);
                if(hashset.find(rem)!=hashset.end()){
                    vector<int>temp={nums[i],nums[j],rem};
                    sort(temp.begin(),temp.end());
                    ans1.insert(temp);
                }
                hashset.insert(nums[j]);
            }
        }
        vector<vector<int>>ans(ans1.begin(),ans1.end());
        return ans;
        */

        //Brute Force by 3 Loops TC- O(n3 logn) and SC-2*O(no of triplets)
    }
};