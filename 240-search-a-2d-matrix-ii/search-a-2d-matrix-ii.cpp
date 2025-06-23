class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        //Optimal by making use of sorted matrix and starting from two of the corner 
        //[0][m-1] or [n-1][0] that are going increasing and decreasing in either directrions
        //TC-O(n + m) and SC-O(1)
        int n = matrix.size();
        int m = matrix[0].size();
        int row = 0; 
        int col = m-1;
        while(row < n && col >= 0){
            if(matrix[row][col]==target){
                return true;
            }
            else if(matrix[row][col] < target){
                row++;
            }
            else{
                col--;
            }
        }
        return false;

        //Better can be done by using a loop for going through the columns and using binary search
        //on each row from i[0] to i[m-1]
        //TC-O(n*logm) SC-O(1)

        //Brute force will be 2 loops and searching 
        //TC- O(n2) and SC - O(1)
    }
};