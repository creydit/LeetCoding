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
    struct Compare{
        bool operator()(ListNode* a, ListNode* b){
            return a->val > b->val;
        }
    };
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        //Better Optimal apporach can be using priroity heap 
        //firstly adding all the nodes of list in queue/heap then taking the smallest out and if it has next
        //putting it into the heap and simultanoeusly doing this 
        //TC - O(n * log(len(lists))) and SC - O(len(lists))
        priority_queue<ListNode* , vector<ListNode*>, Compare> minHeap;
        for(auto i : lists){
            if(i) minHeap.push(i);
        }

        ListNode* dummy = new ListNode(-1);
        ListNode* temp = dummy;
        while(!minHeap.empty()){
            ListNode* newNode = minHeap.top();
            minHeap.pop();
            temp->next = newNode;
            temp = newNode;
            if(newNode->next) minHeap.push(newNode->next);
        }
        return dummy->next;

        //Brute force by me is using a array to hold all the values then sort it and make a new LL
        //TC - O(n*n + n*logn + n) and SC - O(n + n)
        /*
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
        */
    }
};