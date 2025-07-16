class Solution {
public:
    int numberOfSubstrings(string s) {
        //bEtter by little change when we get a all three chars further every string will have them
        //so we can break from there
        //TC - O(n^2) and SC- O(1)
        int n = s.size();
        int ans = 0;
        for(int i = 0; i< n; i++){             
            bool a = false;
            bool b = false;
            bool c = false;
            for(int j = i; j<n; j++){
                if (s[j] == 'a') a = true;
                if(s[j] == 'b') b = true;
                if (s[j] == 'c') c = true;
                if (a && b && c){
                    ans += n-j;
                    break;
                }
            }
        }
        return ans;

        //Brute force using 2 loops scanning throught all the sub string and checking the desired thing
        //TC - O(n^2) and SC - O(1)
        /*
        int n = s.size();
        int ans = 0;
        for(int i = 0; i< n; i++){             
            bool a = false;
            bool b = false;
            bool c = false;
            for(int j = i; j<n; j++){
                if (s[j] == 'a') a = true;
                if(s[j] == 'b') b = true;
                if (s[j] == 'c') c = true;
                if (a && b && c)ans++;
            }
        }
        return ans;
        */
    }
};