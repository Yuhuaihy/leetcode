//Write an algorithm to determine if a number is "happy".

//A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

//Example: 19 is a happy number

//12 + 92 = 82
//82 + 22 = 68
//62 + 82 = 100
//12 + 02 + 02 = 1


// non-happy numbers reach a cycle
class Solution(object):
    def Square(self,n):
        return int(n)*int(n)        
    def Happy(self,n):
        return sum(map(self.Square,list(str(n))))
        
    def isHappy(self, n):    
        numberSet=set()
        while (n>1) and (n not in numberSet):        
            numberSet.add(n)
            n=self.Happy(n)
        if(n == 1):
            return True
        else:
            return False

        
  class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = []
        while(n):
            s = str(n)
            n = sum([int(x) ** 2 for x in s])
            if n not in l:
                l.append(n)
            else:
                break
            
        return n == 1
        
        
