class Solution {
#define ll long long 
public:
    int countIslands(vector<vector<int>>& grid, int k) {
        //BY BFS multisource
        //TC - O(4*N*M ) and SC - O(N*M)
        ll n = grid.size();
        ll m = grid[0].size();
        vector<vector<bool>> vis(n, vector<bool>(m,false));
        ll ans = 0;
        for(ll i = 0; i < n; i++){
            for(ll j = 0; j < m; j++){
                if(!vis[i][j] && grid[i][j] != 0){
                    queue<pair<ll,ll>> q;
                    vis[i][j] = true;
                    q.push({i,j});
                    int dx[] = {-1, 0 , 1, 0};
                    int dy[] = {0, 1, 0, -1};
                    ll sum = 0;
                    while(!q.empty()){
                        ll r = q.front().first;
                        ll c = q.front().second;
                        q.pop();
                        sum += grid[r][c];
                        for(int d = 0; d< 4; d++){
                            ll rr = r + dx[d];
                            ll cc = c + dy[d];
                            if(rr>=0 && cc>=0 && rr<n && cc<m && !vis[rr][cc] && grid[rr][cc] !=0 ){
                                vis[rr][cc] = true;
                                q.push({rr,cc});
                            }
                        }
                    }
                    if(sum % k == 0) ans++;
                }
            }
        }
        return ans;
    }
};