class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        stack = [1]
        while len(stack) <= rowIndex:
            stack.append(1)
            for i in range(len(stack)-1-1,0,-1):
                stack[i] = stack[i] + stack[i-1]
        return stack     
