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
    ListNode* deleteDuplicates(ListNode* head) {
        //Brute force cum optimal solution involving moving the pointer ahead till we find a 
        //non duplicate value of temp and then just connecting the links
        // TC - O(n) and SC - O(1)
        ListNode* temp = head;
        while(temp && temp->next){
            ListNode* nextNode = temp->next;

            while(nextNode && nextNode->val == temp->val ){
                nextNode = nextNode->next;
            }
            temp->next = nextNode;
            temp = temp->next;
        }
        return head;
    }
};