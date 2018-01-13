# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        listA = headA
        listB = headB
        while(listA != listB):
            listA = listA.next if listA else headB
            listB = listB.next if listB else headA
        return listA
 #list 1:m nodes, 2
 #list2: n nodes, 2   last 2 nodes overlap
 #exchange m+n-2 = n + m-2 meet
