class Solution {
public:
    vector<string> ans;
    bool isValid(string &s){
        int cnt=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='('){
                cnt++;
            }
            else{
                cnt--;
            }
            if(cnt<0){
                return false;
            }
        }
        return cnt==0;
    }

    void solve(string &curr, int n){
        if(curr.size()>=2*n){
            if(isValid(curr)){
                ans.push_back(curr);
            }
            return;
        }
        curr.push_back('(');
        solve(curr,n);
        curr.pop_back();

        curr.push_back(')');
        solve(curr,n);
        curr.pop_back();
    }

    vector<string> generateParenthesis(int n) {
        //Recursion approach and Backtracking
        string s;
        solve(s,n);
        return ans;
    }
};