# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #Brute Force using array space
        #TC - O(N + N/2) SC - O(N)
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