class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        if len(self.l) == 0:
            mini = x
        else:
            mini = self.l[-1][1] 
        mini = mini if mini < x else x
        self.l.append((x,mini))
        
        

    def pop(self):
        """
        :rtype: void
        """
        
        return self.l.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.l[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
