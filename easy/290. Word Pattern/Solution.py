class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l = str.split()
        d = {}
        if len(l) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if l[i] in d.values():
                    return False
                else:
                    d[pattern[i]] = l[i]
                
            else:
                if d[pattern[i]] != l[i]:
                    return False
        return True
