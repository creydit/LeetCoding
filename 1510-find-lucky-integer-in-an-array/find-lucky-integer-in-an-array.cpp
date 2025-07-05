class Solution {
public:
    int findLucky(vector<int>& arr) {
        //Brute Force using a map to store all the elements woth there frequencies and then
        //traverse through the map to find the lucky number and check if it's max
        //TC - O(n+set(n)) ~ O(2n) and SC - O(n) for map
        unordered_map<int,int> mpp;
        for(auto i: arr){
            mpp[i]++;
        }
        int ans = -1;
        for(auto [i,j] : mpp){
            if(i==j){
                ans = max(ans,i);
            }
        }
        return ans;
    }
};