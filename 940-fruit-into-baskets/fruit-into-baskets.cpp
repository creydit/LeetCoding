class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        //Optimal solution by changes in sliding window solution
        //TC - O(n) and SC - O(3)
        int n = fruits.size();
        int maxLen = 0;
        int l = 0;
        int r = 0;
        unordered_map<int, int> mpp;
        while( r < n){
            mpp[fruits[r]]++;
            if( mpp.size() > 2){
                mpp[fruits[l]]--;
                if( mpp[fruits[l]] == 0) mpp.erase(fruits[l]);
                l++;
            }
            maxLen = max(maxLen, r - l  + 1);
            r++;
        }
        return maxLen;

        //Better by sliding window approach using a map to store atmost 2 elements
        //TC - O(n + n) and SC - O(3)
        /*
        int n = fruits.size();
        int maxLen = 0;
        int l = 0;
        int r = 0;
        unordered_map<int, int> mpp;
        while(r < n ){
            mpp[fruits[r]]++;
            while( mpp.size() > 2){
                mpp[fruits[l]]--;
                if( mpp[fruits[l]] == 0) mpp.erase(fruits[l]);
                l++;
            }
            maxLen = max(maxLen, r - l + 1);
            r++;
        }
        return maxLen;
        */

        //Brute force (navie) solution is using 2 loops to calculate all the sub arrays 
        //and finding out the maximum length
        //TC - O(n2) and SC - O(3)
        /*
        int n = fruits.size();
        int maxLen = 0;
        for(int i = 0; i < n; i++){
            unordered_set<int> st;
            for(int j = i; j < n; j++){
                st.insert(fruits[j]);
                if(st.size() <= 2){
                    maxLen = max(maxLen, j - i + 1);
                }
                else break;
            }
        }
        return maxLen;
        */
        
    }
};