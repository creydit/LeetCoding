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
    bool isPalindrome(ListNode* head) {
        //Brute force tihnking using a stack to store the values in one traversal 
        //then on 2nd use the top of stack to compare throughout the traversal of the list and if we 
        //found anything non matching then false otheriwse it'll be true
        stack <int> st;
        ListNode* temp = head;
        while(temp){
            st.push(temp->val);
            temp = temp->next;
        }
        temp = head;
        while(temp){
            if( temp->val != st.top()){
                return false;
            }
            temp = temp->next;
            st.pop();
        }
        return true;
    }
};