class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> pref(n,0);
        vector<int> suff(n,0);
        pref[0] = height[0];
        suff[n-1] = height[n-1];
        for(int i = 1; i < n; i++){
            pref[i] = max(pref[i-1], height[i]);
            suff[n-1-i] = max(suff[n-i], height[n-1-i]);
        }
        int ans = 0;
        for(int i = 0; i < n; i++){
            if (height[i] < pref[i] && height[i] < suff[i]){
                ans += min(pref[i],suff[i]) - height[i];
            }
        }
        return ans;
    }
};