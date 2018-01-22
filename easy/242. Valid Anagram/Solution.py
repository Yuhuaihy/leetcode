class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = [0]*26
        n = [0]*26
        if len(s) != len(t):
            return False
        for c in s:
            m[ord(c)-ord('a')] += 1
        for c in t:
            n[ord(c)-ord('a')] += 1
            
        return m == n
        
