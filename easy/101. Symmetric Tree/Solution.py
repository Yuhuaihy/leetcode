# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.isSame(root.left,root.right)
            
    def isSame(self,left,right):
        if (not left) and (not right):
            return True
        elif (not left) or (not right):
            return False
        else:
            return left.val == right.val and self.isSame(left.left, right.right) and self.isSame(left.right,right.left)
