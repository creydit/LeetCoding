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
    ListNode* reverse(ListNode* head){
        ListNode* temp = head;
        ListNode* prev = nullptr;
        while(temp){
            ListNode* front = temp->next;
            temp->next = prev;
            prev = temp;
            temp = front;
        }
        return prev;
    }
    bool isPalindrome(ListNode* head) {
        //Optimal solution will be finding the middle of the list as then reversing the 2nd half 
        //of the list to compare with the first using 2 pointers first second and comparing each value
        //TC-O(n/2 + n/2 + n/2 + n/2) ~ O(2n) and SC - O(1)
        if(head==NULL || head->next==NULL) return true;
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast->next!=NULL && fast->next->next!=NULL){
            slow = slow->next;
            fast = fast->next->next;
        } 
        ListNode* first = head;
        ListNode* newHead = reverse(slow->next);
        ListNode* second = newHead;
        while(second!=NULL){
            if (first->val != second->val){
                reverse(newHead);
                return false;
            } 
            first = first->next;
            second = second->next;
        }
        reverse(newHead);
        return true;

        //Brute force tihnking using a stack to store the values in one traversal 
        //then on 2nd use the top of stack to compare throughout the traversal of the list and if we 
        //found anything non matching then false otheriwse it'll be true
        //TC - O(2n) and SC - O(n) as stack
        /*
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
        */
    }
};