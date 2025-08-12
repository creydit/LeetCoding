class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) { 
        //Better by using a sorting with pair of element and number of indices
        // TC - O(2n + nlogn) and SC - O(n)
        int n = nums.size();
        vector<pair<int,int>> arr;
        for(int i = 0;i < n; i++){
            arr.push_back({nums[i], i});
        }
        sort(arr.begin(), arr.end());
        for(int i = 0; i < n-1; i++){
            if (arr[i].first == arr[i+1].first && abs(arr[i].second - arr[i+1].second) <= k)return true;
        }
        return false;
        //Brute using 2 loops
        //TC - O(n2) and SC - O(1)
        /*
        int n = nums.size();
        for(int i = 0; i < n; i++){
            for(int j = i+1; j < n; j++){
                if (nums[i] == nums[j] && abs(i-j) <= k) return true;
            }
        }
        return false;
        */
    }
};