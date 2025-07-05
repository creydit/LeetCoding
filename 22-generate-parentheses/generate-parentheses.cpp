class Solution {
public:
    vector<string> ans;
    /*
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
    */
    void solve(string &curr, int n,int open,int close){
        if(curr.size() == 2*n){
            ans.push_back(curr);
            return;
        }

        if(open < n){
            curr.push_back('(');
            solve(curr, n , open+1, close);
            curr.pop_back();   
        }
        if(close < open){
            curr.push_back(')');
            solve(curr, n , open, close+1);
            curr.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        //Better Solution same approach but different condition
        //TC - O(2^2n) and SC - O(2n) depth of recursion
        string s;
        int open = 0;
        int close = 0;
        solve(s,n,open,close);
        return ans;
        //Recursion approach and Backtracking
        //TC - O(2^2n * 2n) and SC - O(2*n) for depth of recursion
        /*
        string s;
        solve(s,n);
        return ans;
        */
    }
};