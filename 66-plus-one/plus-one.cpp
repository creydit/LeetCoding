class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        //Optimal approach with for loop traversing from back and adding one 
        //TC - O(n) and SC - O(1)
        int n = digits.size();
        for(int i = n-1; i >= 0; i--){
            if (i==0){
                if(digits[i]==9){
                    digits.insert(digits.begin(),1);
                    digits[1]=0;
                }
                else{
                    digits[i]++;
                }
            }
            else if (digits[i] < 9){
                digits[i]++;
                return digits;
            }
            else{
                digits[i] = 0;
            }
        }
        return digits;
        //Brute force is converting the while array into an int then adding one then
        //converting that int again into an array
        //TC - O(n + n) and SC - O(1) extra
        /*
        long long int ans = 0;
        for(auto i : digits){
            ans*=10;
            ans+=i;
        }
        ans+=1;
        vector<int> arr;
        while (ans>0){
            arr.push_back(ans%10);
            ans = ans/10;
        }
        reverse(arr.begin(),arr.end());
        return arr;
        */
    }
};