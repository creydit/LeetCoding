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
    bool hasCycle(ListNode *head) {
        //Optimal by using a Tortoise and Hare Algo of using 2 pointer one slow (moves 1 step) 
        //and other fast (moves 2 steps)
        //TC ~ O(n) and SC- O(1)
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast!=NULL && fast->next!=NULL){
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) return true;
        }
        return false;

        
        //Brute Force thinking of using a map to store the nodes and mark them as visited or not 
        //and if a already checked nodes comes again we find a loop
        //TC - O(n * 2 * logn) and SC - O(n) as map is used 
        /*
        unordered_map<ListNode* , int> mpp;
        ListNode* temp = head;
        while(temp){
            if(mpp.find(temp)!=mpp.end()){
                return true;
            }
            mpp[temp]++;
            temp = temp->next;
        }
        return false;
        */
    }
};