#Merge two sorted linked lists and return it as a new list. 
#The new list should be made by splicing together the nodes of the first two lists.

#Example:

#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val <= l2.val:
            
            start = r = result = l1
            insert = l2
        else:
            
            start = r = result = l2
            insert = l1
        while  start and insert:
            if insert.val < start.val:
                
                r.next = insert
                r = insert
                p = insert.next
              
                insert.next = start
                insert = p
                               
            else:
                r = start
                start = start.next
        if (not start) and insert:
            r.next = insert
        return result
