class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        collect = collections.defaultdict(list)
        for word in strs:
            letter = [0]*26
            # another solution  sort word 
            for c in word:
                letter[ord(c)-ord('a')] +=1
            collect[tuple(letter)].append(word)
            
        return collect.values()
