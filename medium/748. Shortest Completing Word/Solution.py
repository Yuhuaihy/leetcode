class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        letters = re.sub(r'[^a-zA-Z]',"",licensePlate).lower()
        dictionary = collections.Counter(letters)
        result = ""
        for word in words:
            if not result or len(word) < len(result):
                word = word.lower()
                d1 = collections.Counter(word)
                flag = False
                for letter in dictionary:
                    if letter not in d1 or d1[letter] < dictionary[letter]:
                        flag = True
                        break
                if not flag:
                    if len(word) == len(letters):
                        return word
                    else:
                        if not result or len(word) < len(result):
                            result = word
        return result
                    
                    
