# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Brute forcing by 2 pass and finding the length then dividing it by two
        if not head or not head.next:
            return None
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        mid = n//2
        temp = head
        prev = None
        ahead = head.next
        while mid:
            prev = temp
            temp = temp.next
            ahead = temp.next
            mid -= 1
        prev.next = ahead
        return head