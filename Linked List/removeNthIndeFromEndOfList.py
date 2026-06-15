#Linked List : Remove Nth index from the end of the list

"""
Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current= current.next

        rmIndex = len(nodes) - n
        if rmIndex == 0:
            return head.next

        nodes[rmIndex - 1].next = nodes[rmIndex].next
        return head