class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        //BY BFS
        //TC - O(4 * N*M) and SC - O(N*M)
        int n = mat.size();
        int m = mat[0].size();
        queue<pair<pair<int,int>,int>> q;
        vector<vector<bool>> vis(n, vector<bool>(m,false));
        vector<vector<int>> dist(n, vector<int> (m,0));
        for(int i = 0; i< n; i++){
            for(int j = 0; j< m; j++){
                if(mat[i][j] == 0){
                    q.push({{i,j}, 0});
                    vis[i][j] = true;
                }
            }
        }
        int dx[] = {-1,0,1,0};
        int dy[]= {0,1,0,-1};
        while(!q.empty()){
            int row = q.front().first.first;
            int col = q.front().first.second;
            int steps = q.front().second;
            q.pop();

            dist[row][col] = steps;

            for(int d = 0; d < 4; d++){
                int rr = row + dx[d];
                int cc = col + dy[d];
                if( rr>=0 && cc>=0 && rr<n && cc<m && !vis[rr][cc]){
                    vis[rr][cc] = true;
                    q.push({{rr,cc}, steps + 1});
                }
            }
        }
        return dist;
    }
};