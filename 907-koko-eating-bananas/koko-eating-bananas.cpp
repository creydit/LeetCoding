class Solution {
public:
    //Optimal by Binary Search TC- O(n log(max(piles)))
    long long func(vector<int>& piles, int x){
        long long total=0;
        for(auto i : piles){
            total+=ceil(double(i)/double(x));
        }
        return total;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int low=1;
        int high=-1;
        for(int i=0;i<piles.size();i++){
            if(high<piles[i])high=piles[i];
        }
        int ans=0;
        while(low<=high){
            int mid=(low+high)/2;
            if(func(piles,mid)<=h){
                ans=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return ans;
        
    }
};