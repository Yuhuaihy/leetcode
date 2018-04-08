class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        l = len(s)
        for i in range(int(l/2)):
            if s[i] != s[l-1-i]:
                return False
        return True
        #For example,
#"A man, a plan, a canal: Panama" is a palindrome.
#"race a car" is not a palindrome.
