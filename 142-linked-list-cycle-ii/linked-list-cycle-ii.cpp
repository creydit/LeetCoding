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
        //Brute Force i think is using a map to store all the visited nodes and if s node that already
        //exist in a map comes again there I know it's the starting point of a cycle
        //TC - O(n * 2 * logn) and SC - O(n) as map will store every node in worse case
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
    }
};