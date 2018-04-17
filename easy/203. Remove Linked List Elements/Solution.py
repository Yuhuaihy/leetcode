# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        p = None
        q = None
        first = head
        while head:
            if head.val == val:
                if not p:
                    head = head.next
                    first = head
                else:
                    q = head.next
                    p.next = head.next
                    head  = q
                    
                    
            else:
                p = head
                head = head.next
        return first
