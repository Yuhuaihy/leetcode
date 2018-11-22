class Solution:
    def findLeaves(self, root):
        """
        Given a binary tree, collect a tree's nodes as if you were doing this: 
        Collect and remove all leaves, repeat until the tree is empty.
        :type root: TreeNode
        :rtype: List[List[int]]
        basic idea:
        the depth of leaves is 0, so leave nodes should be added to ans[0], other nodes, depths = max(left, right) + 1
        """
        ans = [[]]
        def removeLeaves(head, ans):
            if not head.left and not head.right:
                depth = 0
                ans[0].append(head.val)
                # print('leave: ', depth, ans)
                return depth
            leftdepth = rightdepth = 0
            if head.left:
                leftdepth = removeLeaves(head.left, ans)
                leftdepth += 1
            if head.right:
                rightdepth = removeLeaves(head.right, ans)
                rightdepth += 1
            depth = max(leftdepth, rightdepth)
            # print(head.val, depth, ans)
            if depth == len(ans):
                ans.append([])
            ans[depth].append(head.val)    
            return depth
        if not root:
            return []
        removeLeaves(root, ans)
        return ans