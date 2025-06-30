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
    //Function to delete Kth Node
    // TC - O(n) and SC - O(1)
    ListNode* delKthNode(ListNode* head, int k){
        if(head == NULL || head->next ==NULL){
            return head;
        }
        if(k==1){
            ListNode* temp = head;
            head = head->next;
            delete temp;
            return head;
        }
        ListNode* temp = head;
        ListNode* prev = nullptr;
        while(temp){
            k--;
            if(k==0){
                prev->next = prev->next->next;
                delete temp;
                return head;
            }
            prev = temp;
            temp = temp->next;
        }
        return head;
    }

    ListNode* removeNthFromEnd(ListNode* head, int n) {
        //Brute Force I can Think of is finding len of the LL and then substracting n from it
        //Then deleting that node form the first using the delKthNode function
        //TC- O(n + n) ~ O(2n) @ 2 pass  and SC-O(1)
        if(head == NULL || head->next == NULL){
                return NULL;
        }
        int len = 1;
        ListNode* temp = head;
        while(temp){
            len++;
            temp = temp->next;
        }
        int f = len - n;
        temp = head;
        return delKthNode(head,f);
    }
};