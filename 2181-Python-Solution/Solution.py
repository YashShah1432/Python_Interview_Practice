# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head.next
        p2 = head.next

        dummy = ListNode(0)
        tail = dummy

        while p2:
            total = 0
            while p2 and p2.val != 0:
                total += p2.val
                p2 = p2.next

            new_node = ListNode(total)
            tail.next = new_node
            tail = new_node

            if p2:
                p2 = p2.next
                p1 = p2
        return dummy.next
