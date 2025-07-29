class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        int n = num.size();
        vector<int> ans(n,0);
        int carry = 0;
        for (int i = n - 1; i >= 0; i--){
            if (i == n - 1){
                ans[i] = (num[i] + k) % 10;
                carry = ( num[i] + k ) / 10;
                continue;
            } 
            if (carry + num[i] > 9){
                ans[i] = (num[i] + carry) % 10;
                carry = ( num[i] + carry) / 10;
            }
            else{
                ans[i] = num[i] + carry;
                carry = carry / 10;
            }
        }
        if (carry != 0){
            while( carry != 0){
                ans.insert(ans.begin(), carry % 10);
                carry = carry / 10;
            }
        }
        return ans;
    }
};