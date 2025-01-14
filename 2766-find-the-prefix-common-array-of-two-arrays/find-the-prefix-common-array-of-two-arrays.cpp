class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        //By me FTS and little editorial
        int n=A.size();
        vector<int>ans(n,0);
        vector<int>hasharr(n+1,0);
        int same=0;
        for(int i=0;i<n;i++){
            hasharr[A[i]]++;
            if(hasharr[A[i]]>=2)same++;
            hasharr[B[i]]++;
            if(hasharr[B[i]]>=2)same++;
            ans[i]=same;
        }
        return ans;
    }
};