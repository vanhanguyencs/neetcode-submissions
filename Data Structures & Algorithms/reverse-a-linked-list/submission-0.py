# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        option 1: convert linked list to list and revert and create another link list
        option 2: in place
        0 1 2 3
        dummy: 
        -1 -> 0 -> 1 -> 2 -> 3
        cur = head
        loop:
        newHead= cur.next (1)
        cur.next = cur.next.next
        newHead.next = head
        head = newHead
        1 (head) -> 0 (cur) -> 2 -> 3
        newHead = 2
        0 point to 3


        """
        cur = head
        while cur and cur.next:
            newHead = cur.next
            cur.next = cur.next.next
            newHead.next = head
            head = newHead
        
        return head
        