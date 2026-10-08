# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head or not head.next:
            return None
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next
        x = l-n+1
        if x==1:
            head = head.next
            return head
        temp = head
        while x-2>0 and temp.next:
            temp = temp.next 
            x -= 1
        if temp.next:
            if temp.next.next:
                temp.next = temp.next.next
            else:
                temp.next = None
        else:
            return None
        return head