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
    /*
    ListNode* collisionP(ListNode* t1, ListNode* t2, int d){
        while(d){
            d--;
            t2 = t2->next;
        }
        while(t1!=t2){
            t1 = t1->next;
            t2 = t2->next;
        }
        return t1;
    }
    */
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        //Optimal Solution is using thwe temp pointer to move in kind of a cycle to cover the 
        //difference in length of the two LL
        //TC - O(n1 + n2) and SC - O(1)
        if(headA == NULL || headB == NULL) return NULL;
        ListNode* t1 = headA;
        ListNode* t2 = headB;
        while(t1 != t2){
            t1 = t1->next;
            t2 = t2->next;

            if(t1 == t2) return t1;
            if(t1 == NULL) t1 = headB;
            if(t2 == NULL) t2 = headA;
        }
        return t1;

        //Better solution involves moving the temp of longer LL to equalize the length of both the list
        //then traverse simultanoeusly and find the intersection point
        //TC - O(n1 + 2n2) and SC - O(1)

        /*
        int n1 = 1;
        int n2 = 1;
        ListNode* temp = headA;
        while(temp){
            n1++;
            temp = temp->next;
        }
        temp = headB;
        while(temp){
            n2++;
            temp = temp->next;
        }
        if (n1 < n2){
            return collisionP(headA , headB, n2-n1);
        }
        else{
            return collisionP(headB, headA, n1-n2);
        }
        */

        //Brute force I can think of using a map to store all the nodes of one list and then
        //traversing through the 2nd list and checking the map if the current node is in it or not
        //if it is there then it will be the intersection point of it 
        //TC - O(n1 *logn1 + n2 * logn2) and SC - O(n)

        /*
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
        */
    }
};