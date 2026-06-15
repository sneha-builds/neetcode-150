# Linked List: Add Two Numbers

"""You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            new_digit = total_sum % 10
            
            current.next = ListNode(new_digit)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy_head.next
        