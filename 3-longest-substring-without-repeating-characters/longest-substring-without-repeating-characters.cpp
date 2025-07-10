class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        //Better by just using 2 loops and not exactly creating sub strings just traversing  
        //through it using the 2nd loop and checking if we have seen a character by using map
        //TC - O(n2) and SC - O(n)
        int n = s.size();
        int ans = 0;
        for(int i = 0 ; i < n; i++){
            unordered_map <char, int> mpp;
            for(int j = i; j < n; j++){
                if(mpp.find(s[j]) != mpp.end()){
                    break;
                }
                mpp[s[j]] = 1;
                ans = max(ans , j - i + 1);
            }
        }
        return ans;
        //Brute force approch making all the substring from s using 2 loops and then
        //traversing through that substring if we find a duplicate character we break and leave that
        //substring and checking of duplication is done by using a map 
        //also we update the ans with max of new string if it is
        // TC - O(n3) amd SC - O(n+n)
        /*
        int n = s.size();
        int ans = -1;
        for(int i = 0; i < n; i++){
            for(int j = i ; j < n; j++){
                string a = s.substr(i,j-i+1);
                unordered_map<char,int> mpp;
                bool f = true;
                for(auto k : a){
                    if(mpp.find(k)!=mpp.end()){
                        f = false;
                        break;
                    }
                    mpp[k] = 1;
                }
                mpp.clear();
                if( f ){
                    ans = max(ans, j-i+1);
                }
            }
        }
        return ans;
        */
    }
};