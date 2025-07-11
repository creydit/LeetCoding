class Solution {
public:
    int maxPower(string s) {
        //Basic traversal and upation of curr if the previous character is equal to the current 
        //wherever it does not reset curr to 1
        //TC - O(n) and SC - O(1);
        int n = s.size();
        int ans = 1;
        int curr = 1;
        for(int i = 1; i < n; i++){
            if(s[i] == s[i-1]){
                curr++;
                ans = max(ans, curr);
            }
            else{
                curr = 1;
            }
        }
        return ans;
    }
};