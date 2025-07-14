class Solution {
public:
    int solve(int n){
        if (n <= 1) return n;
        return solve(n-1) + solve(n-2);
    }

    int fib(int n) {
        //Brute force using plane recursion
        //TC - O(2^n) and SC - O(n) recursion stack space
        return solve(n);
    }
};