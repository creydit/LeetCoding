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
        //Optimal approach involves making new nodes and inserting between the original nodes
        //Then connecting the random pointers to the copy ones 
        //Then finally with the use of dummyNode connecting the next pointer in manner 
        //to generate the new LL
        //TC - O(3n) and SC - O(n) asked in question

        //Making new nodes between old ones
        Node* temp = head;
        while(temp){
            Node* copyNode = new Node(temp->val);
            copyNode->next = temp->next;
            temp->next = copyNode;
            temp = temp->next->next;
        }
        
        //Connecting the random pointers to the copy nodes
        temp = head;
        while(temp){
            Node* copyNode = temp->next;
            if(temp->random){
                copyNode->random = temp->random->next;
            }
            else{
                copyNode->random = nullptr;
            }
            temp = temp->next->next;
        }

        //Connecting the next pointer using dummy Node
        temp = head;
        Node* dummyNode = new Node(-1);
        Node* res = dummyNode;
        while(temp){
            res->next = temp->next;
            temp->next = temp->next->next;

            res = res->next;
            temp = temp->next;
        }
        return dummyNode->next;

        //Brute force of using a map to store both original and copy of node into it 
        //then travsering and making links from original
        //TC - O(n + n + logn) and O(2nlogn) and SC - O(n + n) ~ O(2n) for map and answer

        /*
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
        */
    }
};