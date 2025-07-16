class Solution {
public:
    int numberOfSubstrings(string s) {
        //Optimal solution by slding window and 2 pointer 
        //we are making a least possible sub string which has all 3 chars and then adding the previous
        //all the elements of it
        //TC - O(n) and SC - O(1)
        vector<int> lastSeen(3, -1);
        int ans = 0;
        for(int i = 0; i < s.size(); i++){
            lastSeen[s[i] - 'a'] = i;
            if(lastSeen[0] != -1 && lastSeen[1] != -1 &&lastSeen[2] != -1 ){
                ans += 1 + *min_element(lastSeen.begin(), lastSeen.end());
            }
        }
        return ans;

        //bEtter by little change when we get a all three chars further every string will have them
        //so we can break from there
        //TC - O(n^2) and SC- O(1)
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
                if (a && b && c){
                    ans += n-j;
                    break;
                }
            }
        }
        return ans;
        */

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