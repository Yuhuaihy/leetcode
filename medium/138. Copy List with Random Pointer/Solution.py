# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
#A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#Return a deep copy of the list.

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        begin = result = RandomListNode(head.label)
        node = head
        while node:
            if node.random:
                result.random = RandomListNode(node.random.label)
            if node.next:
                temp = RandomListNode(node.next.label)
                result.next = temp
                result = result.next
            node = node.next
            
        return begin
      ###assumption: no cycle
