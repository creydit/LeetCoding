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
    ListNode* rotateRight(ListNode* head, int k) {
        //Brtue cum Optimal solution as firstly connecting the tail to head then finding the 
        //new last node and assigning head to the newLastNode's next and then making it point to null
        //TC -O( n+n) ~ O(2n) and SC - O(1)
        if(head == NULL || head->next==NULL) return head;
        ListNode* tail = head;
        int len = 1;
        while(tail->next){
            tail = tail->next;
            len++;
        }
        ListNode* temp = head;
        k = k % len;
        if(k == 0) return head;
        int cnt = len - k;
        tail->next = head;
        ListNode* newLastNode = temp;
        while(temp){
            cnt--;
            if(cnt == 0){
                newLastNode = temp;
                break;
            }
            temp = temp->next;
        }
        head = newLastNode->next;
        newLastNode->next = nullptr;
        return head;
    }
};