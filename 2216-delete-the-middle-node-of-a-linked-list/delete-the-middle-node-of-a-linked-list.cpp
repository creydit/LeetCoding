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
    ListNode* deleteMiddle(ListNode* head) {
        //Optimal by using Tortoise and Hare algorithm for finding the middle of the LL
        //with slight changes of skipping one step of slow to get it before the middle 
        //TC - O(n/2) ~O(n) and SC - O(1)
        if(head == NULL || head->next==NULL){
            return NULL;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        fast = fast->next->next;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* delNode = slow->next;
        slow->next = slow->next->next;
        delete delNode;
        return head;

        //Brute force i can think of is findng the len of LL then len/2 then we got to that node 
        //and perform the regular deleting method of nodes woth taken care of edge cases
        //TC - O(n + n/2) ~ O(n) and SC - O(1)

        /*
        if(head==NULL || head->next==NULL){
            return NULL;
        }
        int len = 1;
        ListNode* temp = head;
        while(temp){
            len++;
            temp = temp->next;
        }
        len = (len+1)/2;
        if(len == 1){
            head->next = nullptr;
            return head;
        }
        temp = head;
        ListNode* prev = nullptr;
        while(temp){
            len--;
            if(len==0){
                prev->next = prev->next->next;
                delete temp;
                return head;
            }
            prev = temp;
            temp = temp->next;
        }
        return head;
        */
    }
};