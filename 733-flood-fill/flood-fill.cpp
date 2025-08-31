class Solution {
private: 
    void dfs(int sr, int sc, vector<vector<int>>& ans, vector<vector<int>>& image, int iniC, int nC){
        int n = image.size();
        int m = image[0].size();
        ans[sr][sc] = nC;
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, 1, 0, -1};

        for(int d = 0; d < 4; d++){
            int rr = sr + dx[d];
            int cc = sc + dy[d];
            
            if( rr>=0 && cc>=0 && rr < n && cc < m && ans[rr][cc] != nC && image[rr][cc] == iniC ){
                dfs(rr, cc, ans, image, iniC, nC);
            }
        }
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        //DFS 
        //TC - O( 4*(n*m)) and SC - O(2 *(n*M))
        vector<vector<int>> ans = image;
        int iniC = image[sr][sc];
        dfs(sr, sc, ans, image, iniC, color);
        return ans;
    }
};