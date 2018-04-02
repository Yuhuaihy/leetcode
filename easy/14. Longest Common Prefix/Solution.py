class Solution:
    def isCommon(self,strs,mid):
        s = strs[0][:mid]
        for i in range(len(strs)):
            if s != strs[i][:mid]:
                return False
        return True
            
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        minl = len(strs[0])
        for s in strs:
            minl= min(minl,len(s))
        if not minl :
            return ""
        low = 0
        high = minl
        while( low <= high):
            mid = int((low + high) / 2)
            flag = self.isCommon(strs,mid)
            if flag:
                low = low + 1
            else:
                high = high - 1
        return strs[0][:int((low + high)/2)]
                
