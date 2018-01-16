class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        s = re.sub('\s','',s)  #delete blank
        l = len(s)
        num = []
        operator = []
        while i <l :
            while i<l and s[i]==' ':
                i+=1
            temp = ''
    # match number
            if s[i]>='0' and s[i] <= '9':
                while i < l and (s[i]>='0' and s[i]<='9'):
                    temp += s[i]
                    i += 1
                i -= 1
                num.append(int(temp))    # push number
            else:
                if s[i] == '*' or s[i] == '/':
                    op = s[i]
                    i += 1
                    while i < l and (s[i] >= '0' and s[i] <= '9'):
                        temp += s[i]
                        i += 1
                    tempResult = num.pop() * int(temp) if op == '*' else num.pop() / int(temp)
                    num.append(tempResult)
                    i -= 1
                else:
                    operator.append(s[i])
            i = i+1
        num.reverse()
        operator.reverse()
        while operator:
            r = num.pop() + num.pop() if operator.pop() == '+' else num.pop() - num.pop()
            num.append(r)
        return num.pop()
                    
