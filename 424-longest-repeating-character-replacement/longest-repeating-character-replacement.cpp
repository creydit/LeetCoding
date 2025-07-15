class Solution {
public:
    int characterReplacement(string s, int k) {
        //Better by using sliding window approach to do the same thing as brute storing hash and etc.
        int n = s.size();
        int l = 0;
        int r = 0;
        int ans = 0;
        int maxf = 0;
        vector<int> hash(26, 0);
        while( r < n){
            hash[s[r] - 'A']++;
            maxf = max(maxf, hash[s[r] - 'A']);
            while((r - l + 1) - maxf > k){
                hash[s[l] - 'A']--;
                //maxf = *max_element(hash.begin(), hash.end()); //really dont require this as decreasing wont help in answer
                l++;
            }
            if( (r-l+1) - maxf <= k) ans = max(ans, r-l+1);
            r++;
        }
        return ans;


        //Brute force using 2 loops to generate all the sub strings and then checking
        //the idea of checking here, In characters unlike that in max consecutive ones III is
        //We maintain a hash array to count chars and we will try to replace the less in number chars
        //to the MAX of them thatr is we geting by len(substring) - size of it.
        //TC - O(n^2) and SC - O(26) ~ O(1)
        /*
        int n= s.size();
        int ans = 0;
        for(int i = 0; i < n; i++){
            vector<int> hash(26,0);
            int maxj = 0;
            for(int j = i; j < n; j++){
                hash[s[j] - 'A']++;
                maxj = max(maxj, hash[s[j] - 'A']);
                int changes = (j-i+1) - maxj;
                if( changes <= k) ans = max(ans, j-i+1);
                else break;
            }
        }
        return ans;
        */
    }
};