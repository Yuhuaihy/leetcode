class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = set()
        add = []
        for i in range(len(s)-9):
            temp = s[i:i+10]
            if temp in add:
                result.add(temp)
            else:
                add.append(temp)
            
        return list(result)
