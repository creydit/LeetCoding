class Solution {
public:
    long long numberOfWeeks(vector<int>& milestones) {
        int maxi = INT_MIN;
        long long int ss = 0;
        for (int x : milestones){
            maxi = max(maxi, x);
            ss += x;
        }
        long long int others = ss - maxi;
        if (others >= maxi){
            return ss;
        }
        return 2*others + 1;
    }
};