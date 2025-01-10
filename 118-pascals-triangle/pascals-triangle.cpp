class Solution {
public:
    long long ncr(int n,int r){
        long long res=1;
        for(int i=0;i<r;i++){
            res*=(n-i);
            res/=i+1;
        }
        return res;
    }
    vector<vector<int>> generate(int numRows) {
        //Pascal Triangle formula: (row-1)C(column-1)
        
        //Brute Force by O(n3)
        vector<vector<int>>ans;
        for(int i=1;i<numRows+1;i++){
            vector<int>temp;
            for(int j=1;j<i+1;j++){
                temp.push_back(ncr(i-1,j-1));
            }
            ans.push_back(temp);
        }
        return ans ;
    }
};