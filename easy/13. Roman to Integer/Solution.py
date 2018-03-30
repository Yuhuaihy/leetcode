class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l = ['I','X','C']
        result = 0
        flag = 0 # I X C
        temp = 0
        for element in s:
            if element in l:
                if flag:
                    if temp < d[element]:
                        result = result + d[element] - temp
                        temp = 0
                        flag = 0
                    else:
                        result = result + temp
                        temp = d[element]
                        flag = 1
                else:
                    flag = 1
                    temp = d[element]
            else:
                if temp< d[element]:
                    result = result + d[element] - flag*temp
                else:
                    result = result + d[element] + flag * temp
                flag = 0
                temp = 0
                
        return result+temp
                
        
        
        
