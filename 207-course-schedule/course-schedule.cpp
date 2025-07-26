class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        //BY using Topo Sort
        //TC - O(V + E) and SC - O( V + V*2)
        int n = numCourses;
        vector<vector<int>> adj(n+1);
        for(auto x : prerequisites){
            adj[x[1]].push_back(x[0]);
        }
        //BY BFS
        vector<int> indegree(n,0);
        for(int i = 0; i < n; i++){
            for(auto node : adj[i]){
                indegree[node]++;
            }
        }
        queue<int> q;
        for(int i =0; i < n; i++){
            if(indegree[i] == 0){
                q.push(i);
            }
        }
        int cnt = 0;
        while(!q.empty()){
            int at = q.front();
            q.pop();
            cnt++;

            for(auto next : adj[at]){
                indegree[next]--;
                if( indegree[next] == 0){
                    q.push(next);
                }
            }
        }

        if(cnt == n) return true;
        else return false;
    }
};