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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        //Brute force by me is using a array to hold all the values then sort it and make a new LL
        //TC - O(n*n + n*logn + n) and SC - O(n + n)
        vector<int> arr;
        for(auto i : lists){
            ListNode* temp = i;
            while(temp){
                arr.push_back(temp->val);
                temp = temp->next;
            }
        }
        if (arr.empty()) return nullptr;
        sort(arr.begin(),arr.end());
        ListNode* head = new ListNode(arr[0]);
        ListNode* temp = head;
        for(int i = 1;i<arr.size();i++){
            ListNode* newNode = new ListNode(arr[i]);
            temp->next = newNode;
            temp = newNode;
        }
        return head;
    }
};