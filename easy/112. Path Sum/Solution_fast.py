# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        return self.add(root,sum,0)
        
    def add(self,root,sum,current):
        if not root:
            return False
        if not root.left and not root.right:
            if current + root.val == sum:
                return True
            return False
        
        return self.add(root.left,sum,current + root.val) or self.add(root.right,sum,current + root.val)
        
        
