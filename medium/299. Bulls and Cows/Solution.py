class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)
        numA = [0]*10
        numB = [0]*10
        A = 0
        B = 0
        result = 0
        for i in range(n):
            if secret[i] == guess[i]:
                A +=1
            else:
                numA[int(secret[i])] += 1
                numB[int(guess[i])] += 1
                
        for i in range(10):
            result += numA[i] if numB[i] >= numA[i] else numB[i]
        return str(A)+'A'+str(result)+'B'
            
