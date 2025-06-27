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
        //Brute Force thinking of using a map to store the nodes and mark them as visited or not 
        //and if a already checked nodes comes again we find a loop
        //TC - O(n * 2 * logn) and SC - O(n) as map is used 
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
    }
};