# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def diff(root):
            if not root:
                return 0
            left = diff(root.left) 
            right = diff(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left,right) + 1
        return diff(root) != -1
            
