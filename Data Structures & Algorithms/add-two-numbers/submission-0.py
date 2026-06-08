# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
        sum = 0
        while l1 or l2:
            sum += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.next = ListNode(sum % 10)
            cur = cur.next
            sum //= 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if sum > 0:
            cur.next = ListNode(1)
        
        return dummy.next

