class Solution {
public:
    //Calculation of prime using Sieve of Eratosthene (nloglogn)

    long long splitArray(vector<int>& nums) {
        //By just making sieve and calculating througha  single traversal 
        //TC - O(n + nloglogn) and SC - O(1)
        vector<bool> isPrime(100001, true);
        isPrime[0] = false;
        isPrime[1] = false;
        for(int i = 2; i*i <= 1e5; i++){
            if(isPrime[i]){
                for(int j = i*i; j <= 1e5; j+=i){
                    isPrime[j] = false;
                }
            }
        }
        
        int n = nums.size();
        long long sumA = 0;
        long long sumB = 0;
        for(int i = 0; i < n; i++){
            if(isPrime[i]){
                sumA += nums[i];
            }
            else{
                sumB += nums[i];
            }
        }
        return abs(sumA - sumB);
    }
};