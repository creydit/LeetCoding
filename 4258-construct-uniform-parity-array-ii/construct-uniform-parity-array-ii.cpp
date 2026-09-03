class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        int oddmini=INT_MAX;
        for (auto i : nums1){
            oddmini = min(oddmini, i);
        }
        if(oddmini&1)return true;
        for(auto i : nums1){
            if(i&1)return false;
        }
        return true;
    }
};