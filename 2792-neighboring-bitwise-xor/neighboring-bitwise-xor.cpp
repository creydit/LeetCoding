class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        //By me FTS
        int xr=0;
        for(auto i:derived){
            xr^=i;
        }
        if (xr==0)return true;
        return false;
    }
};