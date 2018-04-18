class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        if n == 3:
            return 1
        prime = [True] * n
        i = 2
        for i in range(2,n/2 + 1):
            j = i * i
            while j < n:
                prime[j] = False
                j = j + i
                
            
        result = prime[2:].count(True) 
        return result
