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
        ListNode* t1 = l1;
        ListNode* t2 = l2;
        ListNode* dummyNode = new ListNode(-1);
        ListNode* temp = dummyNode;
        while(t1 && t2){
            if(t1->val < t2->val){
                temp->next = t1;
                temp = t1;
                t1 = t1->next;
            }
            else{
                temp->next = t2;
                temp = t2;
                t2 = t2->next;
            }
        }
        if(t1){
            temp->next = t1;
        }
        else{
            temp->next = t2;
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