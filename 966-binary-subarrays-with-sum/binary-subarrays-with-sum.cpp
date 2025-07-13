class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        //Better by using mapp and reverse eng
        //TC - O(n) and SC - O(n) due to mpp
        int ans = 0;
        int presum = 0;
        unordered_map<int, int>mpp;
        mpp[0] = 1;
        for(int i = 0; i < nums.size(); i++){
            presum += nums[i];
            int rem = presum - goal;
            ans += mpp[rem];
            mpp[presum]++;
        }
        return ans;
        //Brute force approach involves using 2 loops and making all the sub array then 
        //counting the the sum and if it equals goal then ans++
        //TC - O(n2) and SC - O(1)
        /*
        int n = nums.size();
        int ans = 0;
        for(int  i = 0; i < n; i++){
            int currsum = 0;
            for(int j = i; j < n; j++){
                currsum += nums[j];
                if(currsum == goal){
                ans++;
                }
            }
            
        }
        return ans;
        */
    }
};