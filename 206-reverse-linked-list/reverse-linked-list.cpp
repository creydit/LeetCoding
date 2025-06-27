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
    ListNode* reverseList(ListNode* head) {
        //Brute force i can think of is using a stack to store the elements in
        // in one traversal then on 2nd pop those values from it and upfdate the list
        //TC - O(2n) and SC - O(n)
        stack<int> st;
        ListNode* temp = head;
        while(temp){
            st.push(temp->val);
            temp = temp->next;
        } 
        temp = head;
        while(temp){
            temp->val = st.top();
            st.pop();
            temp = temp->next;
        }
        return head;
    }
};