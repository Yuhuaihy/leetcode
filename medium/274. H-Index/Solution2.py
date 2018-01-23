class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #h papers at least h
        #n-h no more than h
        #extra space
        n = len(citations)
        count = [0]*(n+1)
        result = 0
        for i in citations:
            if i >= n:
                count[n] += 1
            else:
                count[i] += 1
        
        for i in range(n,-1,-1):
            result += count[i]
            if result >= i:
                return i
     
        return 0
        
