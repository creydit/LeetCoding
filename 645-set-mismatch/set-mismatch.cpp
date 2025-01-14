#define ll long long int
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        //Optimalc 1 with maths
        ll n=nums.size();
        ll Sn=(n*(n+1))/2;
        ll S2n=(n*(n+1)*(2*n+1))/6;
        ll Tn=0,T2n=0;
        for(int i=0;i<n;i++){
            Tn+=nums[i];
            T2n+=(nums[i]*nums[i]);
        }
        ll xy=Sn-Tn;
        ll x2y2=S2n-T2n;
        ll xpy=x2y2/xy;
        int x=(xy+xpy)/2;
        int y=x-xy;
        return {y,x};
        //Optimal 2 with XOR
        //Better with hash array TC-O(n) SC-O(n+1)
    }
};