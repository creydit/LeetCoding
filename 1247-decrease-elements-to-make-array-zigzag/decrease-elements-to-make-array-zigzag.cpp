class Solution {
public:
    int movesToMakeZigzag(vector<int>& nums) {
        int n=nums.size();
        int costOdd=0;
        vector<int>temp=nums;
        for(int i=1;i<n;i+=2){
            if(temp[i-1]>=temp[i]){
                costOdd=costOdd+(temp[i-1]-temp[i])+1;
                temp[i-1]=temp[i]-1;
            }
            if(i<n-1 && temp[i+1]>=temp[i]){
                costOdd=costOdd+(temp[i+1]-temp[i])+1;
                temp[i+1]=temp[i]-1;
            }
        }
        int costEven=0;
        temp=nums;
        for(int i=0;i<n;i+=2){
            if(i>0 && temp[i-1]>=temp[i]){
                costEven=costEven+(temp[i-1]-temp[i])+1;
                temp[i-1]=temp[i]-1;
            }
            if(i<n-1 && temp[i+1]>=temp[i]){
                costEven=costEven+(temp[i+1]-temp[i])+1;
                temp[i+1]=temp[i]-1;
            }
        }
        int ans=min(costEven,costOdd);
        return ans;
    }
};