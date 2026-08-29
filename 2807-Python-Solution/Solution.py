# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        if curr == None or curr.next == None:
            return head

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        while curr and curr.next:
            divisor = gcd(curr.val, curr.next.val)
            new_node = ListNode(divisor)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        return head