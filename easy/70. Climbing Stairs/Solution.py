class Solution(object):
  
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int  
       if n == 0 or n == 1:          
            return 1         
        else:
            return self.climbStairs(n-2) + self.climbStairs(n-1)    
       """ 
        a = 1
        b = 1
        while( n > 1):
            temp = b
            b = a + b
            a = temp
            n = n - 1
        
        return b
