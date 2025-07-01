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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        //Brute force I can think of using a map to store all the nodes of one list and then
        //traversing through the 2nd list and checking the map if the current node is in it or not
        //if it is there then it will be the intersection point of it 
        //TC - O(n1 + n2) and SC - O(n)
        unordered_map<ListNode* , int>mpp;
        ListNode* temp = headA;
        while(temp){
            mpp[temp] = 1;
            temp = temp->next;
        }
        temp = headB;
        while(temp){
            if (mpp.find(temp)!=mpp.end()){
                return temp;
            }
            temp = temp->next;
        }
        return nullptr;
    }
};