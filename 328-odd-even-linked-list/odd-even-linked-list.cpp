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
    ListNode* oddEvenList(ListNode* head) {
        //Brute force thinking of using 2 stack to store the values of odd even nodes and 
        //maintaing a counter to record the what is odd and what is even 
        //TC - O(n/2 + n/2 + n) ~ O(2n) and SC - O(n)
        if (head==NULL || head->next==NULL){
            return head;
        }
        vector<int> vec;
        ListNode* temp = head;
        while(temp && temp->next){
            vec.push_back(temp->val);
            temp = temp->next->next;
        }
        if(temp) vec.push_back(temp->val);
        temp = head->next;
        while(temp && temp->next){
            vec.push_back(temp->val);
            temp = temp->next->next;
        }
        if(temp) vec.push_back(temp->val);

        temp = head;
        int i =0;
        while(temp){
            temp->val = vec[i];
            i++;
            temp = temp->next;
        }
        return head;
    }
};