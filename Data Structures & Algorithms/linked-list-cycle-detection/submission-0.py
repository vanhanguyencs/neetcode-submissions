# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        n: len of linked list

        slow x speed
        if there
        fast 2*x speec
        if there is no cyle:
            slow run x
            fast run n: get end of list
        if there is cycle:
            slow run n
            fast run 2n
        example:
        slow: 1, fast 2
        slow 2, fast 4
        slow 3, fast 3 (meet)
        """
        if not head:
            return False
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        