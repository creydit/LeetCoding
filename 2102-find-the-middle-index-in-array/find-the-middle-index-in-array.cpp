class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
        int n = nums.size();
  int total=0;
  for(int i = 0; i<n; i++){
  	total += nums[i];
  }
  int leftSum=0, rightSum=0;
  for(int i = 0; i<n; i++){
  	rightSum = total - nums[i] - leftSum;
    
    
    if(leftSum == rightSum)return i;
    leftSum+=nums[i];
  }
  return -1;
    }
};