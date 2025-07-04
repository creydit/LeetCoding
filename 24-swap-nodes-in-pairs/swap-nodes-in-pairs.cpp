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
    ListNode* swapPairs(ListNode* head) {
        //Optimal solution by changing link of nodes in pairs with use of dummy node and 4 pointer
        //pointing to prev , curr (temp) and 2 fronts next and next to next
        // TC - O(n) and SC - O(1)
        if(head == NULL || head->next == NULL){
            return head;
        }
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* temp = head;
        ListNode* prev = dummy;
        while(temp && temp->next){
            ListNode* front1 = temp->next;
            ListNode* front2 = temp->next->next;
            front1->next = temp;
            temp->next = front2;
            prev->next = front1;

            prev = temp;
            temp = front2;
        }
        return dummy->next;

        //Brute force i can think of is using a array to store the values then swapping adjacent 
        //then again replacing it in the LL
        //TC O(n+n+n) ~ O(3n) and SC - O(n)

        /*
        if(head == NULL || head->next == NULL){
            return head;
        }
        vector<int> arr;
        ListNode* temp = head;
        while(temp){
            arr.push_back(temp->val);
            temp = temp->next;
        }
        for(int i=0; i<arr.size()-1; i+=2){
            swap(arr[i],arr[i+1]);
        }
        temp = head;
        int i=0;
        while(temp){
            temp->val = arr[i];
            i++;
            temp = temp->next;
        }
        return head;
        */
    }
};