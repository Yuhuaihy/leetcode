class Solution(object):
    def countAndSay(self, n):
        re = {}
        re[1] = "1"
        
        for i in range(2,n+1):
            re[i] = self.call(re[i-1])
        return re[n]
                
    def call(self,s):
        n = len(s)
        temp = s[0]
        count = 1
        result = ""
        for i in range(1,n):
            if s[i] != temp:
                result = result + str(count) + temp
                temp = s[i]
                count = 1
            else:
                count +=1
                
        result = result + str(count) + temp       
        return result
        
        
        
