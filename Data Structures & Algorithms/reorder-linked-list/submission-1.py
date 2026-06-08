# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        2 4 6 8
        slow = 2, fast 2
        slow = 4, fast 6

        2 4 6 8 10
        slow = 2 fast = 2
        slow = 4, fast = 6
        slow = 6, fast = 10

        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse slow.next to end
        # e.g 1, 2, 3, 4
        """
        cur = newHead = 1
        nex = 2
        1 -> 3 -> 4
        2 -> 1 -> 3 -> 4
        newHead = 2, cur = 1
        nex = 3
        1 -> 4
        3 -> 2 -> 1 -> 4
        newHead = 3 cur = 1
        nex = 4
        1 -> null
        4 -> 3 -> 2 -> 1 -> null
        """
        newHead = slow.next
        slow.next = None
        cur = newHead
        while cur and cur.next:
            nex = cur.next
            cur.next = cur.next.next
            nex.next = newHead
            newHead = nex
        """
        1 -> 2 -> 3
        6 -> 5 -> 4

        temp = newHead
        newHead = newHead.next
        temp.next = cur.next
        cur.next = temp
        cur = cur.next.next

        """
        cur = head
        while newHead:
            temp = newHead
            newHead = newHead.next
            temp.next = cur.next
            cur.next = temp
            cur = cur.next.next

        
