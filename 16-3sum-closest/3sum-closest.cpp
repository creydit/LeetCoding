class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        //Optimising using 2 pointers qnd sorting
        //TC - O(n2 + nlogn) and SC - O(1)
        int n = nums.size();
        int ans = 0;
        int gap = INT_MAX;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < n; i++){
            int j = i + 1;
            int k = n - 1;
            while( j < k){
                long long sum = nums[i];
                sum += nums[j];
                sum += nums[k];

                int req = abs(sum - target);
                if(req < gap){
                    gap = req;
                    ans = sum;
                }
                if( sum > target){
                    k--;
                }
                else if ( sum < target){
                    j++;
                }
                else{
                    j++;
                    k--;
                }
            }
        }
        return ans;

        //Brute force using 3 loops
        //TC - O(n3) and SC - O(1)
        /*
        int n = nums.size();
        int ans = 0;
        int gap = INT_MAX;
        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                for(int k = j + 1; k < n; k++){
                    long long sum = nums[i];
                    sum += nums[j];
                    sum += nums[k];
                    if( abs(sum - target) < gap){
                        gap = abs(sum - target);
                        ans = sum;
                    }
                }
            }
        }
        return ans;
        */
        
    }
};