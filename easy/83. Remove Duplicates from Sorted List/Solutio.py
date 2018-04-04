#Given a sorted linked list, delete all duplicates such that each element appear only once.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        first = head
        p = head
        head = head.next
        while(head):
            if p.val != head.val:
                p.next = head
                p = p.next
                
                head = head.next
            else:
                head = head.next
        p.next = None
        return first
