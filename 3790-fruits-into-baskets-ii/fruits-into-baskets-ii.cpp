class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        //Brute force approach by using 2 loops
        //TC - O(n2) and SC - O(1000)
        int n = fruits.size();
        int ans = 0;
        for(int i = 0; i < n; i++){
            bool f = true;
            for(int j = 0; j < baskets.size(); j++){
                if(baskets[j] >= fruits[i]){
                    baskets.erase(baskets.begin() + j);
                    f = false;
                    break;
                }
            }
            if(f) ans++;
        }
        return ans;
    }
};