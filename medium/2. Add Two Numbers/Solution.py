# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        resultFirst = t = ListNode(0)
        while l1 or l2:
            add1 = l1.val if l1 else 0
            add2 = l2.val if l2 else 0
            temp = add1 + add2 + carry
            carry = temp/10
            node = temp%10
            t.next = ListNode(node)
            t = t.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            tList = ListNode(1)
            t.next = tList
        return resultFirst.next
