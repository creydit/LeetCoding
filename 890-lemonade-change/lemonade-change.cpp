class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        //Simple greddy solution 
        //TC - O(n) and SC - O(2) 
        vector<int> mpp(2,0);
        int n = bills.size();
        for(int i = 0; i <n; i++){
            if(bills[i] == 5){
                mpp[0]++;
            }
            else if(bills[i] == 10){
                if(mpp[0] != 0){
                    mpp[0]--;
                    mpp[1]++;
                }
                else return false;
            }
            else{
                if(mpp[0] != 0){
                    if(mpp[1] != 0){
                        mpp[0]--;
                        mpp[1]--;
                    }
                    else{
                        if(mpp[0] > 1){
                            mpp[0]--;
                            if(mpp[0]==0) return false;
                            mpp[0]--;
                            if(mpp[0]==0) return false;
                            mpp[0]--;
                        }
                        else{
                            return false;
                        }
                    }
                }
                else return false;
            }
        }
        return true;
    }
};