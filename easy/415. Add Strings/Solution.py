class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1)
        j = len(num2)
        carry = 0
        result = ''
        
        while(i>0 or j>0):
            i-=1
            j-=1
            n = int(num1[i]) if i>=0 else 0
            m = int(num2[j]) if j>=0 else 0
            temp = n + m + carry
            carry = temp/10
            result = str(temp%10) + result
        if carry==1:
            result = '1' + result
       
        return result
            
