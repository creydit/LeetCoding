class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.size();
        int ans = 0;
        int left = 0;
        int right = 0;
        for(auto i : s){
            if(i=='('){
                left++;
            }
            else{
                right++;
            }
            if(left==right){
                ans = max(ans, left+right);
            }
            if (right > left){
                left = 0;
                right = 0;
            }
        }
        left = 0;
        right = 0;
        for(int i = n-1; i >= 0; i--){
            if (s[i]=='('){
                left++;
            }
            else{
                right++;
            }
            if(left == right){
                ans = max(ans, left+right);
            }
            if (right < left){
                left = 0;
                right = 0;
            }
        }
        return ans;
    }
};