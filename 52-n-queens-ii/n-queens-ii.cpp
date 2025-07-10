class Solution {
public:
    void solve(int col, vector<string> &board, vector<vector<string>> &ans, vector<int> &leftRow, 
                vector<int> &UpDia, vector<int> &LoDia, int n){
        if( col == n){
            ans.push_back(board);
            return;
        }

        for(int row = 0; row < n; row++){
            if(leftRow[row] == 0 && LoDia[row+col] == 0 && UpDia[n-1 + col-row] ==0 ){
                board[row][col] = 'Q';

                leftRow[row] = 1;
                LoDia[row + col] = 1;
                UpDia[n-1 + col-row] = 1;
                solve(col + 1, board, ans, leftRow, UpDia, LoDia, n);

                board[row][col] = '.';
                leftRow[row] = 0;
                LoDia[row + col] = 0;
                UpDia[n-1 + col-row] = 0;

            }
        }
    }
    int totalNQueens(int n) {
        //Recursion and Backtracking 
        //TC - O(2^n)
        vector<vector<string>> ans;
        vector<string> board(n);
        string s(n, '.');
        for(int i = 0; i < n; i++){
            board[i] = s;
        }
        vector<int> leftRow(n,0);
        vector<int> UpDia(2*n - 1, 0);
        vector<int> LoDia(2*n - 1, 0);
        solve(0, board, ans, leftRow, UpDia, LoDia, n);
        return ans.size();
    }
};