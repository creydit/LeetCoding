# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #Brute using arrays as space
        # TC - O(2N) and SC - O(N)
        small = []
        big = []
        temp = head
        while temp:
            if temp.val < x:
                small.append(temp.val)
            else:
                big.append(temp.val)
            temp = temp.next

        temp = head
        n = len(small)
        nn = len(big)
        idx = 0
        idx2 = 0
        while temp:
            if idx < n:
                temp.val = small[idx]
                idx += 1
            elif idx2 < nn:
                temp.val = big[idx2]
                idx2 += 1
            temp = temp.next
        return head