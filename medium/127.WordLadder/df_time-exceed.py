class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        self.n = len(wordList)
        s = set(wordList)
        self.end = endWord
        visit = {}
            
    
        def find(word, wordlist, visit):
            if word == self.end:
                return 1
            

            temp = []
            for i in range(len(word)):
                for c in list('qwertyuiopasdfghjklzxcvbnm'):
                    if c == word[i]:
                        continue
                    temp_word = word[:i] + c + word[i+1:]
                    if temp_word in wordlist and visit.get(temp_word,False) == False:
                        visit[temp_word] = True
                        res = find(temp_word, wordlist, visit)
                        if res:
                            temp.append(1+res)
                        
                        visit[temp_word] = False
                       
                        
            return min(temp) if temp else 0
        return find(beginWord, s, visit)
