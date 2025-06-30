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
    ListNode* middle(ListNode* head){
        ListNode* slow = head;
        ListNode* fast = head->next;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
    ListNode* merge(ListNode* l1 , ListNode* l2){
        ListNode* dummyNode = new ListNode(-1);
        ListNode* temp = dummyNode;
        while(l1 && l2){
            if(l1->val < l2->val){
                temp->next = l1;
                temp = l1;
                l1 = l1->next;
            }
            else{
                temp->next = l2;
                temp = l2;
                l2 = l2->next;
            }
        }
        if(l1){
            temp->next = l1;
        }
        else{
            temp->next = l2;
        }
        return dummyNode->next;
    }
    ListNode* sortList(ListNode* head) {
        //Optimal approach is using merge sort exactly and using a merge node fucntion
        //TC - O(logn * (n + n/2)) and SC - O(1)
        if(head == NULL || head->next == NULL){
            return head;
        }
        ListNode* mid = middle(head);
        ListNode* right = mid->next;
        mid->next = nullptr;
        ListNode* left = head;
        ListNode* leftHead = sortList(left);
        ListNode* rightHead = sortList(right);
        return merge(leftHead,rightHead);

        //Brute force i can think of using a vector to store the elements of LL and then 
        //sorting the vector and then replacing the values in the LL 
        // TC - (n + nlogn + n) ~ O(nlogn) and SC - O(n)

        /*
        vector<int> arr;
        ListNode* temp = head;
        while(temp){
            arr.push_back(temp->val);
            temp = temp->next;
        }
        sort(arr.begin(),arr.end());
        temp = head;
        int i = 0;
        while(temp){
            temp->val = arr[i];
            i++;
            temp = temp->next;
        }
        return head;
        */
    }
};