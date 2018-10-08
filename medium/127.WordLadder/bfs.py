class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        ##BFS
        stack =[]
        steps = 1
        s = set(wordList)
        ind = 0
        prev_ind = 0
        
        prev_len = 1
        sub = 1
        
        visit = {}
        stack.append(beginWord)
        while True:
            word = stack[ind]
            
            for i in range(len(word)):
                for c in list('qwertyuiopasdfghjklzxcvbnm'):
                    if c == word[i]:
                        continue
                    temp_word = word[:i] + c + word[i+1:]
                    if temp_word in s and visit.get(temp_word, False) == False:
                        visit[temp_word] = True
                        if temp_word == endWord:
                            steps += 1
                            return steps
                        stack.append(temp_word)
            ind += 1
            if ind - prev_ind == sub:
                prev_ind = ind
                sub = len(stack) - prev_len
                prev_len = len(stack)
                steps += 1
                # print(stack)
                
            if sub == 0:
                break
        return 0
