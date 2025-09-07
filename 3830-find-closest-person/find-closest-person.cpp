class Solution {
public:
    int findClosest(int x, int y, int z) {
        //Basic maths
        int ans1 = abs(x-z);
        int ans2 = abs(y-z);
        if (ans1 == ans2) return 0;
        if (ans1 > ans2) return 2;
        return 1;
    }
};