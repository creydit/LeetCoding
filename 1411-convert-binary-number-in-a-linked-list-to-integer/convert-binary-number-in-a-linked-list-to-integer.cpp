/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        //Brute force is making a array and then coverting it to int 
        //TC - O(n + n) ~ O(2n) and SC - O(n)
        vector<int> arr;
        int ans = 0; 
        ListNode* temp = head;
        while(temp){
            arr.push_back(temp->val);
            temp = temp->next;
        }
        for(int i = 0;i < arr.size(); i++){
            ans = ans * 2 + arr[i];
        }
        return ans;
    }
};