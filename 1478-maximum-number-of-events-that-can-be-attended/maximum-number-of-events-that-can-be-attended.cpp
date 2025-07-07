class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        //Better or optimal uses priority queue
        //T - O(nlogn + maxDay logn) and SC - O(n)
        int n = events.size();
        int maxDay = 0;
        for (int i = 0; i < n; i++) {
            maxDay = max(maxDay, events[i][1]);
        }
        priority_queue<int, vector<int>, greater<>> pq;
        sort(events.begin(), events.end());
        int ans = 0;
        for (int i = 0, j = 0; i <= maxDay; i++) {
            while (j < n && events[j][0] <= i) {
                pq.push(events[j][1]);
                j++;
            }
            while (!pq.empty() && pq.top() < i) {
                pq.pop();
            }
            if (!pq.empty()) {
                pq.pop();
                ans++;
            }
        }

        return ans;
        //Brute force using a map to store the events attendted on that days
        //TC- O(nlogn + n * d) and SC - O(n) where d is max interval 
        /*
        sort(events.begin(), events.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1]; // sort by end day
        });
        unordered_map<int,int> mpp;
        int ans = 0;
        for(int i = 0; i<events.size(); i++){
            for(int j=events[i][0]; j<=events[i][1];j++){
                if(mpp.find(j)==mpp.end()){ 
                    ans++;
                    mpp[j] = 1;
                    break;
                }
            }
        }
        return ans;
        */
    }
};