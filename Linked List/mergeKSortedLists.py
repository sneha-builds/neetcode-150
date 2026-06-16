#Merge K Sorted Linked Lists

"""
You are given an array of k linked lists lists, where each list is sorted in ascending order.
Return the sorted linked list that is the result of merging all of the individual linked lists.
"""

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lt in lists:
            while lt:
                nodes.append(lt.val)
                lt = lt.next
        nodes.sort()

        res= ListNode(0)
        current = res
        for node in nodes:
            current.next = ListNode(node)
            current=current.next
        return res.next
        