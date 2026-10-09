class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        long long sum = mass;
        sort(asteroids.begin(),asteroids.end());
        for(auto ast : asteroids){
            if (sum < ast) return false;
            sum += ast;
        }
        return true;
    }
};