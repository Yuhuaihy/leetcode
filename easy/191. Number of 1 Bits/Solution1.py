### n & (n - 1)  turn the least significate 1 to 0
## 100 & 011 = 000
#Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

#For example, 
#the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            n = n & (n - 1)
            result += 1
        return result
            
        
