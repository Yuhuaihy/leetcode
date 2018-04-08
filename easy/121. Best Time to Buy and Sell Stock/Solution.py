class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        soFar = 0
        minPrice = prices[0]
        for n in prices:
            if minPrice > n:
                minPrice = n
            
            soFar = max(soFar, n - minPrice)
        return soFar
