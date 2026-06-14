# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #Optimal without extra space using Flyod Tortoise and HAre Algo with Reversal of first half
        #TC - O(N) and SC - O(1)
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next
            
        ans = 0
        while slow:
            ans = max(ans, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        
        return ans

        #Brute Force using array space
        #TC - O(N + N/2) SC - O(N)
        '''
        arr = []
        temp = head
        n = 0
        while temp:
            arr.append(temp.val)
            n += 1
            temp = temp.next
        ans = 0
        for i in range(n//2):
            ans = max(ans, arr[i] + arr[n-1-i])
        return ans 
        '''