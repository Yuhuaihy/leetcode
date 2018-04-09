class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        ## find 5
        # n/ 5
        # n / 25 ...
        while n:
            result = result + n / 5
            n = n / 5
        return result
    #Given an integer n, return the number of trailing zeroes in n!.

