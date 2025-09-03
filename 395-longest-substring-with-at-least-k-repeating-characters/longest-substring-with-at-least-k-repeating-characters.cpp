class Solution {
public:
    int longestSubstring(string s, int k) {
        //Sliding window
        //TC - O(26*n) and SC - O(26)
        int n = s.size();
        int ans = 0;
        int totalUnique = unordered_set<char>(s.begin(), s.end()).size();

        for(int targetUnique = 1; targetUnique <= totalUnique; targetUnique++){
            vector<int> freq(26, 0);
            int l = 0;
            int r = 0;
            int unique = 0;
            int atleastK = 0;

            while( r < n){
                if (freq[s[r] - 'a'] == 0) unique++;
                freq[s[r] - 'a']++;

                if(freq[s[r] - 'a'] == k) atleastK++;

                r++;

                while ( unique > targetUnique){
                    if( freq[s[l] - 'a'] == k) atleastK--;
                    freq[s[l] - 'a']--;
                    if( freq[s[l] - 'a'] == 0) unique--;
                    l++;
                }

                if(unique == targetUnique && unique == atleastK){
                    ans = max(ans, r - l);
                }

            }
        }
        return ans;
    }
};