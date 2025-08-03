class Solution {
public:
    int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
        //By codestorywithMK explaination
        //TC - O(k*logn + n) and SC - O(2n)
        int n = fruits.size();
        vector<int> psum(n);
        vector<int> pos(n);

        for(int i = 0; i < n; i++){
            pos[i] = fruits[i][0];
            psum[i] = fruits[i][1] + (i > 0 ? psum[i-1] : 0);
        }
        int ans = 0;
        for(int d = 0; d <= k/2; d++){
            //Case 1 - moving left first
            int remain = k - 2*d;
            int i = startPos - d;
            int j = startPos + remain;
            
            int left = lower_bound(pos.begin(), pos.end(), i) - pos.begin();
            int right = upper_bound(pos.begin(), pos.end(), j) - pos.begin() - 1;

            if( left <= right){
                int basket = psum[right] - (left > 0 ? psum[left - 1] : 0);
                ans = max(ans, basket);
            }

            //Case 2 - moving right first
            i = startPos - remain;
            j = startPos + d;
            left = lower_bound(pos.begin(), pos.end(), i) - pos.begin();
            right = upper_bound(pos.begin(), pos.end(), j) - pos.begin() - 1;

            if( left <= right){
                int basket = psum[right] - (left > 0 ? psum[left - 1] : 0);
                ans = max(ans, basket);
            }
        }
        return ans;
    }
}; 