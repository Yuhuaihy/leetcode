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
        #dfs
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        stack = []
        sumList = []
        sumList.append(root.val)
        stack.append((0,root))
        
        while stack:
            level,tree = stack.pop()
            if len(sumList) < level + 1:
                sumList.append(sumList[level-1] + tree.val)
            else:
                if level != 0:
                    sumList[level] = sumList[level-1] + tree.val
            
            if  not tree.left and not tree.right and sumList[level] == sum:
                return True
            
            if tree.right:
                stack.append((level + 1, tree.right))
            if tree.left:
                stack.append((level + 1, tree.left))
        return False
            
