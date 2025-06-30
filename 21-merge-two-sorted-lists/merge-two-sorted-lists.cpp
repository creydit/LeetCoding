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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        //Brute force using a vector to store all the nodes of both the list and then sorting them
        //then replacing the values of it
        //TC - 
        vector<int> arr;
        ListNode* temp1 = list1;
        if(list1==NULL){
            if(list2==NULL) return nullptr;
            else{
                return list2;
            }
        }
        if(list2 == NULL){
            return list1;
        }
        //connecting the 2 lists
        while(temp1->next!=NULL){ 
            temp1 = temp1->next;
        }
        temp1->next = list2;
        ListNode* temp2 = list1;
        //adding nodes into arr
        while(temp2){
            arr.push_back(temp2->val);
            temp2 = temp2->next;
        }
        sort(arr.begin(),arr.end());
        //replacing elements
        temp2 = list1;
        int i=0;
        while(temp2){
            temp2->val = arr[i];
            i++;
            temp2 = temp2->next;
        }
        return list1;

    }
};