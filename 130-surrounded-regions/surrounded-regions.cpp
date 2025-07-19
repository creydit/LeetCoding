class Solution {
public:
    void dfs(int r, int c, vector<vector<char>> &board, vector<vector<bool>> &vis){
        int n = board.size();
        int m = board[0].size();
        vis[r][c] = true;
        int dx[] ={-1,0,1,0};
        int dy[] ={0,-1,0,1};

        for(int d = 0; d < 4; d++){
            int rr = r + dx[d];
            int cc = c + dy[d];

            if(rr>=0 && cc>=0 && rr < n && cc < m && !vis[rr][cc] && board[rr][cc] == 'O' ){
                dfs(rr, cc, board, vis);
            }
        }
    }
    void solve(vector<vector<char>>& board) {
        //BY DFS and runnning through all borders and finding their connected Os and marking them
        //except them all the Os will be converted to X
        //TC - O(n + n + 4*n*m) and SC - O(n * m)
        int n = board.size();
        int m = board[0].size();
        vector<vector<bool>> vis(n, vector<bool>(m,false));
        for(int j = 0; j < m; j++){
            if(!vis[0][j] && board[0][j] == 'O'){
                dfs(0, j, board, vis);
            }
            if(!vis[n-1][j] && board[n-1][j] == 'O'){
                dfs(n-1, j, board, vis);
            }
        }

        for(int i = 0; i< n; i++){
            if(!vis[i][0] && board[i][0] == 'O'){
                dfs(i, 0, board, vis);
            }
            if(!vis[i][m-1] && board[i][m-1] == 'O'){
                dfs(i, m-1, board, vis);
            }
        }

        for(int i = 0; i <n; i++){
            for(int j = 0; j < m; j++){
                if(!vis[i][j]){
                    board[i][j] = 'X';
                }
            }
        }
    }
};