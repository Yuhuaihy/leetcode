class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        # 0-25    A-Z
        while(n != 0):
            reminder = n % 26
            n = n // 26
            if reminder == 0 :
                s = 'Z' + s
                
                if n <= 26 and n != 1:
                    s = chr(64 + n - 1) + s
                    n = 0
                else:
                    n = n - 1
                
            else:
                s = chr(64 + reminder) + s
               
            
        
        return s
