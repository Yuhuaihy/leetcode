class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
      
        stack = []       
        if not root:
            return result
        stack.append((root,0))
        while(stack):
            
            tree,d = stack.pop()
         
            if tree :
                if len(result) < d+1 :
                    result.append([])
                result[d].append(tree.val)
                stack.append((tree.right,d+1))
                stack.append((tree.left,d+1))
           
        
        return list(reversed(result))
