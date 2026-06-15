# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Optimal by using Flyod Tortoise and Hare Algorithm to find mid of LL 
        #TC - O(N) and SC - O(1)
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return head



        #Brute forcing by 2 pass and finding the length then dividing it by two
        #TC - O(N + N/2) and SC - O(1)
        '''
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
        '''