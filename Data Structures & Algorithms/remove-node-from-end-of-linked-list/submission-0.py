# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1 2 3 4 5 6 7 8
        size = 8
        nth = 2
        n = 8?
        two pointers
        slow = fast = dummy
        for i in range(size - n):
            fast = fast.next
        fast.next = fast.next.next

        """
        dummy = fast = ListNode(0)
        fast.next = head
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        for _ in range(size - n):
            fast = fast.next
        fast.next = fast.next.next
        return dummy.next