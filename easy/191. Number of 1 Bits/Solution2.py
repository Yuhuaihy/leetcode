class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        a = 1
        for i in range(32):
            if n & a:
                result += 1
            a <<= 1
            
       
        return result
            
