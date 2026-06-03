# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #good sawal
        temp = head
        st = []
        while temp:
            st.append(temp)
            temp = temp.next
        
        curr = st.pop()
        maxi = curr.val
        newHead = ListNode(maxi)
        while st:
            curr = st.pop()
            if curr.val < maxi:
                continue
            else:
                node = ListNode(curr.val)
                node.next = newHead
                newHead = node
                maxi = curr.val
        return newHead

        
            