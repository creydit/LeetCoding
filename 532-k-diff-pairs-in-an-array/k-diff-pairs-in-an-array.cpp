class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        //Optimal solution by using map to store and check if the need = (nums[i] - k) is there 
        //for us if yes that means we got a pair
        // TC - O(n) and SC - O(n)
        int n = nums.size();
        unordered_map<int,int> mpp;
        int ans = 0;
        for(int i = 0; i<n ;i++){
            mpp[nums[i]]++;
        }

        for(auto [i,j] : mpp){
            if (k==0){
                if(j>1)ans++;
            }
            else{
                if(mpp.find(i+k)!=mpp.end()){
                    ans++;
                }
            }
        }
        return ans;

        //Brute force can be using two loops to check every pair of elments in nums
        // TC - O(n2) and SC - O(1)
    }
};