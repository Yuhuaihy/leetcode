class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = 0
        if not a:
            return b
        if not b:
            return a
        
        l1 = len(a)
        l2 = len(b)
        l = max(l1,l2)
        result = ""
        for i in range(l):
            add1 = 0
            add2 = 0
            if i<l1:
                add1 = int(a[l1-1-i])
            if i<l2:
                add2 = int(b[l2-1-i])
            
            add = add1 ^ add2 ^ c
            c = (add1 & add2) | ((add1 | add2) & c) 
            result = str(add) + result
        if c:
            result = "1" + result
        return result
                
                
        
        
