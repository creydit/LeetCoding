class Solution {
public:
    void rotate(vector<vector<int>>& matrix){
        //Optimal Solution by transpose and reversing
        int n=matrix.size();
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                swap(matrix[i][j],matrix[j][i]);
            }
        }
        for(int i=0;i<n;i++){
            reverse(matrix[i].begin(),matrix[i].end());
        }

        //Brute Force by creating a ans matrix and placing the corresponding elements
        //SC - O(n2) not require in answer
        /*
        vector<vector<int>>ans;
        int n=matrix.size();
        int m=matrix[0].size();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                ans[i][n-1-i]=matrix[i][j];
            }
        }
        */
    }
};