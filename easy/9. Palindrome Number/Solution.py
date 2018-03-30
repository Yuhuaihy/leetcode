class Solution:
    def isPalindrome(self, x):
        
        """
        :type x: int
        :rtype: bool
        """
        if (x<0 or (x!= 0 and x % 10 == 0) ):
            return False
        rev = 0
        head = x
        while(rev < head):
            rev = rev*10 + head%10
            head = int(head/10)
        
        return (rev == head) or (int(rev/10) == head)
            
        
        

