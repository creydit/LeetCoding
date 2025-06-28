/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        //Optimal solution by tortoise and hare algorithm using 2 pointer one moving
        //slow (1 step at a time) and another moving fast (2 step at a time) and after collision 
        //moving one of them at the start of the list and letting both of them moving one step at a time 
        //the next time they'll meet will be the starting of the loop 
        //TC - O(n) and SC- O(1)
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast!=NULL && fast->next!=NULL){
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast){
                slow = head;
                while(slow != fast){
                    slow = slow->next;
                    fast = fast->next;
                }
                return slow;
            }
        }
        return nullptr;

        //Brute Force i think is using a map to store all the visited nodes and if s node that already
        //exist in a map comes again there I know it's the starting point of a cycle
        //TC - O(n * 2 * logn) and SC - O(n) as map will store every node in worse case
        /*
        unordered_map<ListNode* ,int>mpp;
        ListNode* temp = head;
        while(temp){
            if (mpp.find(temp)!=mpp.end()){
                return temp;
            }
            mpp[temp]=1;
            temp = temp->next;
        }
        return nullptr;
        */
    }
};