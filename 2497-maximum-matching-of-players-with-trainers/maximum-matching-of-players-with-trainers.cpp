class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        //Brute force  - Optimal approach by 2 pointer and greedy
        //TC - O(nlogn + mlogm + min(n,m)) and SC - O(1)
        sort(players.begin(), players.end());
        sort(trainers.begin(), trainers.end());
        int n = players.size();
        int m = trainers.size();
        int l = 0;
        int r = 0;
        while(l < n && r < m){
            if( players[l] <= trainers[r]) l++;
            r++;
        }
        return l;
    }
};