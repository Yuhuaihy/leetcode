#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #stack ({[ push, ]}) pop
        l = list()
        d = {'(':0,'[':1,'{':2,')':0,']':1,'}':2}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                l.append(c)
            else:
                if not l:
                    return False
                else:
                    t = l.pop()
                    if d[c] != d[t]:
                        return False
        if not l:
            return True
        else:
            return False
