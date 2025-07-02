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
    ListNode* getKthNode(ListNode* temp, int k){
        k--;
        while(temp && k>0){
            k--;
            temp = temp->next;
        }
        return temp;
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        //Brute Force thought was actual optimal - like sending k group to rerverse function 
        //simultanoeus links changes works everything
        //TC - O(n+n) ~ O(2n) and SC - O(1)
        if(head == NULL || head->next == NULL){
            return head;
        }
        ListNode* temp = head;
        ListNode* prevNode = nullptr;
        while(temp){
            ListNode* KthNode = getKthNode(temp,k);
            if(KthNode == NULL){
                if(prevNode) prevNode->next = temp;
                break;
            }
            ListNode* nextNode = KthNode->next;
            KthNode->next = nullptr;
            reverse(temp);
            if(temp == head){
                head = KthNode;
            }
            else{
                prevNode->next = KthNode;
            }
            prevNode = temp;
            temp = nextNode;
        }
        return head;
    }
};