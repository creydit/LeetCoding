class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        string ans = "";
        int maxi = 0;
        int start = 0;
        int end = 0;
        for(int i = 0; i < n; i++){
            //odd 
            int left = i;
            int right = i;
            while (left >= 0 && right < n && s[left]==s[right]){
                if (right - left + 1 > maxi){
                    maxi = right - left + 1;
                    start = left;
                    end = right;
                }
                left -= 1;
                right += 1;
            }
            //even
            left = i-1;
            right = i;
            while (left >= 0 && right < n && s[left]==s[right]){
                if (right - left + 1 > maxi){
                    maxi = right - left + 1;
                    start = left;
                    end = right;
                }
                left -= 1;
                right += 1;
            }
        }
        for(int i = start; i <= end; i++) ans += s[i];
        return ans;

    }
};