class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int n=arr.size();
        vector<int> dupArray(n);
        int i=0, j=0;
        while(j<n){
            if(arr[i]!=0){
            dupArray[j]=arr[i];
            i++;
            j++;
            }
             else{
                dupArray[j]=0;
            if(j==(n-1))break;
            else {
                dupArray[j+1]=0;
                i++;
                j+=2;
            }
            if(j>=n)break;
            }
        }
        for(int i=0; i<n; i++){
            arr[i]=dupArray[i];
        }
    }
};