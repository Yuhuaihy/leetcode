# easy 
# use sort
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        c = sorted(citations,reverse=True)
        n = len(c)
        #h papers at least h
        #n-h no more than h
        for i in range(n):
            if i < n-1 and i+1 <= c[i] and  i+1 >= c[i+1]:
                return i+1
            elif i == n-1 and c[i] >= i+1:
                return i+1
        
        if n ==1:
            return 1 if c[i]>0 else 0
        
        return 0
