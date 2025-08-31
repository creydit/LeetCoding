class Solution {
public:
    int candy(vector<int>& ratings) {
        //Better by removing the right array 
        //TC - O(2n) and SC- O(n)
        int n = ratings.size();
        vector<int> left(n , 0);
        left[0] = 1;
        for(int i = 1; i < n; i++){
            if( ratings[i] > ratings[i-1]){
                left[i] = left[i-1] + 1;
            }
            else{
                left[i] = 1;
            }
        }
        int right = 1;
        int ans = max(1, left[n-1]);
        for(int i = n-2; i >= 0; i--){
            if( ratings[i] > ratings[i+1]){
                right += 1;
            }
            else{
                right = 1;
            }
            ans += max(right, left[i]);
        }
        return ans;

        //Brute Force using both directional traversal and keeping arrays to give candies
        //then taking max of both the answer
        //TC - O(3n) and SC - O(2n)
        /*
        int n = ratings.size();
        vector<int> left(n , 0);
        vector<int> right(n, 0);
        left[0] = 1;
        right[n-1] = 1;
        for(int i = 1; i < n; i++){
            if( ratings[i] > ratings[i-1]){
                left[i] = left[i-1] + 1;
            }
            else{
                left[i] = 1;
            }
        }

        for(int i = n-2; i >= 0; i--){
            if( ratings[i] > ratings[i+1]){
                right[i] = right[i+1] + 1;
            }
            else{
                right[i] = 1;
            }
        }
        int ans = 0;
        for(int i = 0; i < n; i++){
            ans += max(left[i], right[i]);
        }
        return ans;
        */


    }
};