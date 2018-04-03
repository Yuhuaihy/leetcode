class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x == 1:
            return x
        low = 1
        high = x
        while(low < high):
            mid = int((low + high) / 2)
            if(mid * mid > x):
                high = mid
            elif (mid * mid < x):
                low = mid + 1
            else:
                return mid
            
        return low-1
                
        
        
