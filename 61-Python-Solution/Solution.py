# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        curr = head
        prev = None
        count = 0

        if p1 == None or p1.next == None or k == 0:
            return head

        while curr:
            curr = curr.next
            count += 1
        
        k %= count
        if k == 0:
            return head
            
        for i in range(k):
            p1 = p1.next
        
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        new_head = p2.next
        p2.next = None
        p1.next = head
        return new_head     