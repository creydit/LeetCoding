/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        //Brute force of using a map to store both original and copy of node into it 
        //then travsering and making links from original
        //TC - O(n + n + logn) and O(2nlogn) and SC - O(n + n) ~ O(2n) for map and answer
        Node* temp = head;
        unordered_map<Node*,Node*>mpp;
        while(temp){
            Node* newNode = new Node(temp->val);
            mpp[temp] = newNode;
            temp = temp->next;
        }
        temp = head;
        while(temp){
            Node* copyNode = mpp[temp];
            copyNode->next = mpp[temp->next];
            copyNode->random = mpp[temp->random];
            temp = temp->next;
        }
        return mpp[head];
    }
};